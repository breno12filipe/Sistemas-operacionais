import threading # importa a biblioteca de threads
semaforo = threading.Semaphore() # retorna um objeto do tipo semaforo
valor = 0 
class Conta():
    def __init__(self,saldo):
        self.saldo = saldo

def transferencia(conta1,conta2):
    if conta1.saldo >= valor:
        semaforo.acquire() # bloqueia a "trava" do semaforo, ou seja bloqueia as threads 
        conta1.saldo = conta1.saldo - valor
        conta2.saldo = conta2.saldo + valor
        print("Saldo conta 1",conta1.saldo)
        print("Saldo conta 2",conta2.saldo)
        semaforo.release()# desbloqueia a "trava" do semaforo, ou seja desbloqueia as threads
        
if __name__ == '__main__':
    conta_from = Conta(100)
    conta_to = Conta(100)
    valor = 10

    for i in range (0,10):
        thrd = threading.Thread(target = transferencia(conta_from,conta_to))# retorna uma thread
                                                                            # passando como parametro
                                                                            # a função de transferencia
                                                                            
        thrd.start # começa a atividade da thread

    
        
    
