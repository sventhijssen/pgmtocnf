from Encoding import Encoding1, Encoding2
from Variables import ParameterVariable
from Graph import Node
from Instance import Instance

def main(graph):
    #print("===")
    #print("CNF - ENC1")
    #print("===")
    #enc1 = Encoding1(graph)
    #for clause in enc1.get_cnf():
    #    print(clause)
    #enc1.export_to_dimacs("out/enc1.cnf")
    #enc1.export_enc_to_latex("out/enc1_enc.tex")
    #enc1.export_weights_to_latex("out/enc1_weights.tex")

    #weights = enc1.get_weights()
    #for weight in weights:
    #    print(weight)

    #print("===")
    #print("CNF - ENC2")
    #print("===")
    #enc2 = Encoding2(graph)
    #for clause in enc2.get_cnf():
    #    print(clause)
    #enc2.export_to_dimacs("out/enc2.cnf")
    #enc2.export_enc_to_latex("out/enc2_enc.tex")
    #enc2.export_weights_to_latex("out/enc2_weights.tex")

    #weights = enc2.get_weights()
    #for weight in weights:
    #    print(weight)

    #graph_type = graph.get_type()

    encodings = [Encoding1(graph), Encoding2(graph)]

    for encoding in encodings:
        enc_name = encoding.get_enc_name()
        graph_type = graph.get_graph_type()
        print("===")
        print("CNF")
        print(enc_name)
        print(graph_type)
        print("===")
        encoding = Encoding1(graph)
        for clause in encoding.get_cnf():
            print(clause)
        path = "C:/Users/User/Documents/Informatica/2018-2019/capita-selecta/Probabilistic Programming/PySDD/"
        #path = "out/"
        file_name = path + enc_name + "_" + graph_type
        encoding.export_enc_to_latex(file_name)
        encoding.export_to_dimacs(file_name)
        encoding.export_to_dimacs(file_name, 'pysdd')
        encoding.export_to_dimacs(file_name, 'cachet')
        encoding.export_weights_to_latex(file_name)

        weights = encoding.get_weights()
        for weight in weights:
            print(weight)
