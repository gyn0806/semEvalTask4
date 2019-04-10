import json

class Instance(object):
    """
    A single training/test example for the Squad dataset.
    For examples without an answer, the start and end position are -1.
    """

    def __init__(self, text, tag, id):
        self.text = text
        self.tag = tag
        self.id = id
        # print(self.start_position)

    
def dumps(source_data, output_path):
    return open(output_path,"w").write(json.dumps({"data":[instance.__dict__ for instance in source_data]}))


def preprocess(mode, path,opt_path):
	raw_data = [line.strip() for line in open(path).readlines()]
	instances = []
	for index, line in enumerate(raw_data):
		try:
			id, tag, text = line.split( maxsplit = 2)
			instances.append(Instance(id = id, tag = tag, text = text))
		except Exception as e:
			print(index)
			print(line)
			exit()
	return instances


	

if __name__ == '__main__':
	mode = "test"
	path = "./data/" + mode + ".txt"
	opt_path = "./data/" + mode + ".json"
	source_data = preprocess(mode = mode, path = path, opt_path = opt_path )
	dumps(source_data, opt_path)
