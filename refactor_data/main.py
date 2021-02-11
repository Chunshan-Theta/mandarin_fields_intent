import csv
import json

def to_col(data: list):

    # check count is equal
    default_cut = None
    for row in data:
        default_cut = len(row) if default_cut is None else default_cut
        assert len(row) == default_cut

    #
    cols = [[] for _ in range(default_cut)]
    for idx in range(default_cut):
        for row in data:
            cols[idx].append(row[idx])

    #
    res = []
    for col in cols[1:]:
        if col[2] != '':
            res.append(
                {
                    "type": col[2],
                    "sub_type": col[3],
                    "examples": [i for i in col[4:] if i != '']
            })

    #
    return res


def to_train(row:list):
    def replace_type(type_name):
        doc = {
        }
        return doc[type_name] if type_name in doc else type_name

    def write_file(rows, file_name):
        with open(f"train-{file_name}.tsv", 'w') as fd:
            for row in rows:
                tags = str(row[0]).replace("'","")
                fd.write(f"{tags}\t{row[1]}")
                fd.write("\n")

    res_dict = {}
    for t in row:
        t_type = replace_type(t["type"])
        t_sub_type = replace_type(t["sub_type"])
        for example in t["examples"]:
            if example not in res_dict:
                res_dict[example] = {
                    "t_type": [],
                    "t_sub_type": []
                }
            res_dict[example]["t_type"].append(t_type)
            res_dict[example]["t_sub_type"].append(t_sub_type)
    # print(json.dumps(res_dict, ensure_ascii=False))

    #
    rows = []
    for k in res_dict.keys():
        rows.append([res_dict[k]['t_type'], k])
    write_file(rows, 't_type')

    #
    rows = []
    for k in res_dict.keys():
        rows.append([res_dict[k]['t_sub_type'], k])
    write_file(rows, 't_sub_type')


with open("data.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    class_examples = to_col(list(rd))
    to_train(class_examples)
