def calcula_area_perimetro(dimensoes):
    largura, comprimento = dimensoes
    area = largura * comprimento
    perimetro = 2 * (largura + comprimento)
    return area, perimetro
