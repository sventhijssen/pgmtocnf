from Encoding import Encoding1, Encoding2


def main(graph):
    print("===")
    print("CNF - ENC1")
    print("===")
    enc1 = Encoding1(graph)
    for clause in enc1.get_cnf():
        print(clause)
    enc1.export_to_dimacs("out/enc1.cnf")
    enc1.export_enc_to_latex("out/enc1_enc.tex")
    enc1.export_weights_to_latex("out/enc1_weights.tex")

    weights = enc1.get_weights()
    for weight in weights:
        print(weight)

    print("===")
    print("CNF - ENC2")
    print("===")
    enc2 = Encoding2(graph)
    for clause in enc2.get_cnf():
        print(clause)
    enc2.export_to_dimacs("out/enc2.cnf")
    enc2.export_enc_to_latex("out/enc2_enc.tex")
    enc2.export_weights_to_latex("out/enc2_weights.tex")

    weights = enc2.get_weights()
    for weight in weights:
        print(weight)
