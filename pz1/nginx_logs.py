from itertools import islice
final = {}

gen_line = (line for line in open('nginx_logs.txt'))
for line in islice(gen_line, None):
    for el in line:
        if el == '-':
            id = line.index(el)
            final[("remote_addr")] = line[0:id]
            break
    for el in line:
        if el == '"':
            id = line.index(el)
            final[('request_type')] = line[id + 1: id + 4]
            break
    for el in line:
        if el == 'd':
            id = line.index(el)
            final[("requested_resource")] = line[id: id + 19]
            out_final = (final["remote_addr"], final["request_type"], final["requested_resource"])
            print(out_final)
            break






