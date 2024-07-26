#© 2024 MaJunYoung akwns615@gmail.com v10 24.07.26
import subprocess, re, sys
print("☆ SK C&C Security Team - Cipher Checker 2024 WITH sslyze ☆")

'''
sktest를 환경변수에 등록하여 사용시 cipher.js를 찾지 못하는 문제가 발생하여 일단 보류, 하드코딩으로 처리
def read_file_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # 줄바꿈 문자를 제거하고 리스트에 저장
    lines = [line.strip() for line in lines]
    return lines

secures = read_file_to_list('cipher.js')
'''

secures = ['TLS_ECCPWD_WITH_AES_128_GCM_SHA256', 'TLS_ECCPWD_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_ECDSA_WITH_ARIA_128_GCM_SHA256', 'TLS_ECDHE_ECDSA_WITH_ARIA_256_GCM_SHA384', 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256', 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384', 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256', 'TLS_ECDHE_PSK_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_PSK_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256', 'TLS_ECCPWD_WITH_AES_128_CCM_SHA256', 'TLS_ECCPWD_WITH_AES_256_CCM_SHA384', 'TLS_ECDHE_ECDSA_WITH_AES_128_CCM', 'TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8', 'TLS_ECDHE_ECDSA_WITH_AES_256_CCM', 'TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8', 'TLS_ECDHE_PSK_WITH_AES_128_CCM_8_SHA256', 'TLS_ECDHE_PSK_WITH_AES_128_CCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384', 'TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384', 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256', 'TLS_AES_128_GCM_SHA256', 'TLS_AES_256_GCM_SHA384', 'TLS_CHACHA20_POLY1305_SHA256', 'TLS_AES_128_CCM_8_SHA256', 'TLS_AES_128_CCM_SHA256']

def main():
    if len(sys.argv) < 2:
        print('!!! How to use !!! : [sktest majun.com] || [sktest majun.com:443]')
        sys.exit(1)
    else:
        del sys.argv[0]
        run_exe(sys.argv)


def run_exe(_list):
    command = ['./data/sslyze.exe']
    command = command + _list
    text1 = "SCAN RESULTS FOR " + command[1]
    print("-"*len(text1))
    print(text1)
    print("-"*len(text1))
    result = subprocess.run(command, capture_output=True, text=True)
    #print(type(result.stdout))
    output = result.stdout
    a = output.split("\n")
    for index, i in enumerate(a):
        if "* TLS 1.1 Cipher Suites:" in i or "* TLS 1.2 Cipher Suites:" in i or "* TLS 1.3 Cipher Suites:" in i:
            if "The server accepted the following" in a[index+3]:
                count = re.search(r'\d+', a[index+3])
                howmany = int(count.group())
                for j in range(4 + howmany):
                    if j > 3:
                        if any(secure in a[index+j] for secure in secures):
                            print("     [SECURE]", a[index+j])
                        else:
                            print("     [WEAK]  ", a[index+j])
                    else:
                        print(a[index+j])
                print("")
            else:
                print(a[index])
                print(a[index+1],"\n")

if __name__ == '__main__':
    main()
