from Encoding import Encoding1, Encoding2


def main(name, graph, evidence=None):

    encodings = [Encoding1(graph, evidence), Encoding2(graph, evidence)]

    for encoding in encodings:
        enc_name = encoding.get_enc_name()
        graph_type = graph.get_graph_type()
        print("===")
        print("CNF")
        print(enc_name)
        print(graph_type)
        print("===")
        for clause in encoding.get_cnf():
            print(clause)
        path = "C:/Users/User/Documents/Informatica/2018-2019/capita-selecta/Probabilistic Programming/PySDD/"
        #path = "out/"
        file_name = path + name + "_" + enc_name + "_" + graph_type
        encoding.export_enc_to_latex(file_name)
        encoding.export_to_dimacs(file_name)
        encoding.export_to_dimacs(file_name, 'pysdd')
        encoding.export_to_dimacs(file_name, 'cachet')
        encoding.export_weights_to_latex(file_name)

        weights = encoding.get_weights()
        for weight in weights:
            print(weight)
