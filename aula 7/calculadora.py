import math
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    # Operações que usam apenas o primeiro número (num1)
    if operacao == "sqrt":
        if num1 < 0:
            return render_template(
                "calculadora.html",
                etapas=f"Não existe raiz real de {num1}.",
                resultados="Erro: número negativo",
            )
        resultado = math.sqrt(num1)
        return render_template(
            "calculadora.html",
            etapas=f"√{num1} = {resultado}",
            resultados=resultado,
        )

    # Operações que exigem obrigatoriamente o segundo número (num2)
    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados="Erro",
        )
    num2 = float(num2_valor)

    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"

    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"

    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} × {num2} = {resultado}"

    elif operacao == "/":
        if num2 == 0:
            return render_template(
                "calculadora.html",
                etapas=f"{num1} ÷ 0",
                resultados="Erro: Divisão por zero",
            )
        resultado = num1 / num2
        etapas = f"{num1} ÷ {num2} = {resultado}"

    elif operacao == "**":
        try:
            resultado = math.pow(num1, num2)
            etapas = f"{num1} ^ {num2} = {resultado}"
        except OverflowError:
            return render_template(
                "calculadora.html",
                etapas=f"{num1} ^ {num2}",
                resultados="Erro: Número muito grande",
            )

    elif operacao == "log":
        # num1 é o argumento, num2 é a base
        if num1 <= 0 or num2 <= 0 or num2 == 1:
            return render_template(
                "calculadora.html",
                etapas=f"log_{num2}({num1})",
                resultados="Erro: Base ou argumento inválidos",
            )
        resultado = math.log(num1, num2)
        etapas = f"log na base {num2} de {num1} = {resultado}"

    else:
        return render_template(
            "calculadora.html", etapas="Operação inválida.", resultados="Erro"
        )

    return render_template(
        "calculadora.html", etapas=etapas, resultados=resultado
    )
