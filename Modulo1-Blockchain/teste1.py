import hashlib

def proof_of_work(previous_proof):
    new_proof = 1
    check_proof = False

    while check_proof is False:
        hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
        if hash_operation[:4] == '0000':
            check_proof = True
        else:
            new_proof += 1

        print(hash_operation)

    print('Sucesso!')
    return new_proof


resp = int(input('Digite um número: '))

proof_of_work(resp)
