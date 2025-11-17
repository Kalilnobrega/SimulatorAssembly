from flask import Flask, request, jsonify
from flask_cors import CORS
from Simulador import Simulator

app = Flask(__name__)
CORS(app)

vm = Simulator()

@app.route("/load", methods=["POST"])
def load_program():
    
    try:
        data = request.get_json()
        code = data.get("code", "")

        if not code.strip():
            return jsonify({"error": "Nenhum código recebido"}), 400

        vm.load_program_from_text(code)

        return jsonify({"status": "program loaded", "instructions": len(vm.program)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route("/run", methods=["POST"])
def run_program():

    try:
        vm.run()
        return jsonify({
            "status": "program executed",
            "registers": vm.cpu.dump()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500