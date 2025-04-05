from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/dados', methods=['POST'])
def receber_dados():
    dados = request.json
    nome = dados.get('nome')
    idade = dados.get('idade')
    return idade,nome

@app.route('/api/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'visitante')
    return jsonify({'mensagem': f'Olá, {nome}! Seja bem-vindo.'})










#############################################################################################

#if __name__ == '__main__':
#    app.run(debug=True)
