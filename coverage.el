;; -*- coding: utf-8; lexical-binding: t -*-
;; :Project:   pglast -- Show coverage stats in the fringe
;; :Created:   gio 19 mar 2020, 09:12:15
;; :Author:    Lele Gaifax <lele@metapensiero.it>
;; :License:   GNU General Public License version 3 or later
;; :Copyright: © 2020, 2021 Lele Gaifax
;;

;; Got inspiration from https://github.com/AdamNiederer/cov

(require 'cl-lib)
(require 'filenotify)
(require 'json)
(require 'seq)

(defgroup pycov nil
  "The group for everything in pycov.el"
  :group 'tools)

(defgroup pycov-faces nil
  "Faces for cov."
  :group 'pycov)

(defcustom pycov-excluded-line-fringe-symbol 'question-mark
  "The symbol to display on each excluded line while in pycov-mode."
  :tag "Excluded lines fringe symbol"
  :group 'pycov
  :type 'symbol)

(defcustom pycov-executed-line-fringe-symbol 'filled-rectangle
  "The symbol to display on each executed line while in pycov-mode."
  :tag "Executed lines fringe symbol"
  :group 'pycov
  :type 'symbol)

(defcustom pycov-missing-line-fringe-symbol 'filled-rectangle
  "The symbol to display on each not executed line while in pycov-mode."
  :tag "Missing lines fringe symbol"
  :group 'pycov
  :type 'symbol)

(defface pycov-line-excluded-face
  '((((class color)) :foreground "blue"))
  "Fringe indicator face used for excluded lines."
  :tag "Excluded lines symbol face"
  :group 'pycov)

(defface pycov-line-executed-face
  '((((class color)) :foreground "green"))
  "Fringe indicator face used in coverage mode for executed lines."
  :tag "Executed lines symbol face"
  :group 'pycov)

(defface pycov-line-missing-face
  '((((class color)) :foreground "red"))
  "Fringe indicator face used in coverage mode for not executed lines."
  :tag "Missing lines symbol face"
  :group 'pycov)

(defvar-local pycov-coverage-file nil
  "The path of the file containing coverage statistics in JSON format.")

(put 'pycov-coverage-file 'safe-local-variable 'stringp)

(cl-defstruct pycov-data
  (mtime
   nil
   :documentation "The timestamp of the file.")
  (statistics
   nil
   :documentation "An hash table containing statistics keyed by source file name.")
  (buffers
   nil
   :documentation "A sequence of buffers associated with these statistics.")
  (watcher
   nil
   :documentation "The filenotify descriptor, if possible."))

(defvar pycov-coverages (make-hash-table :test 'equal)
  "Storage of coverage data, keyed by JSON file name.")

(defun pycov--load-statistics (coverage-file)
  "Parse python-coverage statistics stored in COVERAGE-FILE.

Return a list of (FILE . LINES), with LINES being a list
of (LINE-NUM LINE-STAT)), where LINE-STAT is a symbol, either
`executed', `missing' or `excluded'."
  (let* ((json-object-type 'alist)
         (json-array-type 'vector)
         (json-key-type 'string)
         (coverage (json-read-file coverage-file))
         (matches (list)))
    (dolist (source (cdr (assoc "files" coverage)))
      (let ((name (car source))
            (data (cdr source))
            (file-coverage (list)))
        (seq-do (lambda (lineno) (push (cons lineno 'executed) file-coverage))
                (cdr (assoc "executed_lines" data)))
        (seq-do (lambda (lineno) (push (cons lineno 'missing) file-coverage))
                (cdr (assoc "missing_lines" data)))
        (seq-do (lambda (lineno) (push (cons lineno 'excluded) file-coverage))
                (cdr (assoc "excluded_lines" data)))
        (push (cons name (sort file-coverage (lambda (x y) (< (car x) (car y)))))
              matches)))
    matches))

(defun pycov--watcher (event)
  "Trigger an update of coverage statistics when the JSON source changes."
  (let ((event-type (nth 1 event))
        (event-file (nth 2 event))
        (retry-again 3))
    (when (and (member event-type '(created changed))
               (gethash event-file pycov-coverages))
      (message "File %s changed, reloading and refreshing..." event-file)
      (while (> retry-again 0)
        (condition-case err
            (progn
              (pycov--get-data event-file)
              (setq retry-again 0))
          (json-error
           (message "Parse error, probably due to incomplete write...")
           (setq retry-again (1- retry-again))
           (if (zerop retry-again)
               (message "... giving up after three attempts!")
             (message "... will retry after a micro sleep")
             (sleep-for 0.4))))))))

(defun pycov--get-data (coverage-file)
  (let* ((data (gethash coverage-file pycov-coverages))
         (buffers (and data (pycov-data-buffers data)))
         (watcher (and data (pycov-data-watcher data))))
    (when (and data
               (not (equal (pycov-data-mtime data)
                           (file-attribute-modification-time
                            (file-attributes coverage-file)))))
      (setq data nil))
    (unless data
      (let ((base-dir (file-name-directory coverage-file))
            (mtime (file-attribute-modification-time
                    (file-attributes coverage-file)))
            (statistics (make-hash-table :test 'equal)))
        (dolist (entry (pycov--load-statistics coverage-file))
          (let ((source (expand-file-name (car entry) base-dir)))
            (puthash source (cdr entry) statistics)))
        (when (and file-notify--library (not watcher))
          (setq watcher (file-notify-add-watch base-dir '(change) #'pycov--watcher)))
        (setq data (make-pycov-data :mtime mtime
                                    :statistics statistics
                                    :buffers buffers
                                    :watcher watcher))
        (puthash coverage-file data pycov-coverages)
        (dolist (buffer buffers)
          (with-current-buffer buffer
            (pycov--on)))))
    data))

(defun pycov--make-overlay (line fringe)
  "Create an overlay for the specified LINE with the given FRINGE."
  (let ((ol (save-excursion
              (goto-char (point-min))
              (forward-line (1- line))
              (make-overlay (point) (line-end-position)))))
    (overlay-put ol 'before-string fringe)
    (overlay-put ol 'pycov t)
    ol))

(defun pycov--get-fringe (line-stat)
  "Return the fringe with the correct face for LINE-STAT."
  (let (sym face)
    (cond
     ((eq line-stat 'executed)
      (setq sym pycov-executed-line-fringe-symbol)
      (setq face 'pycov-line-executed-face))
     ((eq line-stat 'missing)
      (setq sym pycov-missing-line-fringe-symbol)
      (setq face 'pycov-line-missing-face))
     ((eq line-stat 'excluded)
      (setq sym pycov-excluded-line-fringe-symbol)
      (setq face 'pycov-line-excluded-face)))
    (propertize "f" 'display `(left-fringe ,sym ,face))))

(defun pycov--first-visible-line ()
  "Determine the first visible source line, taking into account narrowing."
  (let ((start (point-min)))
    (if (= start 1)
        0
      (save-excursion
        (save-restriction
          (widen)
          (1- (line-number-at-pos start)))))))

(defun pycov--add-overlays ()
  "Add pycov overlays."
  (if pycov-coverage-file
      (let ((data (pycov--get-data pycov-coverage-file)))
        (if data
            (let* ((first-visible-line (pycov--first-visible-line))
                   (max-line (+ (line-number-at-pos (point-max)) first-visible-line))
                   (lines (gethash (buffer-file-name) (pycov-data-statistics data)))
                   (buffers (pycov-data-buffers data)))
              (dolist (line lines)
                (when (and (> (car line) first-visible-line)
                           (<= (car line) max-line))
                  (pycov--make-overlay (- (car line) first-visible-line)
                                       (pycov--get-fringe (cdr line)))))
              (if buffers
                  (unless (member (current-buffer) buffers)
                    (setf (pycov-data-buffers data) (push (current-buffer) buffers)))
                (setf (pycov-data-buffers data) (list (current-buffer)))))
          (message "No coverage data found for %s in %s."
                   (buffer-file-name)
                   pycov-coverage-file)))
    (message "Cannot decorate %s, pycov-coverage-file not set." (buffer-file-name))))

(defun pycov--remove-overlays ()
  "Remove all pycov overlays."
  (remove-overlays (point-min) (point-max) 'pycov t))

(defun pycov--on ()
  "Refresh pycov overlays."
  (pycov--remove-overlays)
  (pycov--add-overlays))

(defun pycov--off ()
  "Remove pycov overlays."
  (when pycov-coverage-file
    (let* ((data (gethash pycov-coverage-file pycov-coverages))
           (buffers (and data (pycov-data-buffers data))))
      (when (and buffers (member (current-buffer) buffers))
        (setq buffers (remove (current-buffer) buffers))
        (setf (pycov-data-buffers data) buffers)
        (unless buffers
          (let ((watcher (pycov-data-watcher data)))
            (when watcher
              (file-notify-rm-watch watcher)
              (setf (pycov-data-watcher data) nil))))))
    (pycov--remove-overlays)))

;;;###autoload
(define-minor-mode pycov-mode
  "Minor mode that displays coverage statistics in the fringe."
  :lighter " C"
  (progn
    (if pycov-mode
        (pycov--on)
      (pycov--off))))

(provide 'pycov)
