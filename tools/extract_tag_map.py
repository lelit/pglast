
import sys
import json
import pprint

sys.path.insert(0, './pglast/')
import enums

def workhorse(args):
    with open(args.json_file) as f:
        sdef = json.loads(f.read())

    the_map = {}
    for folderkey, folder in sdef.items():
        for node_key, node_val in folder.items():
            if 'fields' in node_val:
                for f in node_val['fields']:
                    if 'name' in f and 'c_type' in f:
                        if f['c_type']!='NodeTag' and hasattr(
                                enums, f['c_type']):
                            the_map[(node_key, f['name'])] = f['c_type']

    with open(args.output,'w') as f:
        f.write('tag_map = ')
        f.write(pprint.pformat(the_map))







def main():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(description="PG enum extractor",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('json_file',
                        help="struct_defs.json file")
    parser.add_argument('output',
                        help="Python source to be created")

    args = parser.parse_args()

    workhorse(args)


if __name__ == '__main__':
    main()
