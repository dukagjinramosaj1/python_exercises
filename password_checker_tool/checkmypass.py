import requests
import hashlib
import sys

#Establish connection to API with the corresponding values
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, check the API and try again')
    return response

#Get the password hashes and the number of counts on how many times in Count var
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
        # print(h, count)    

#based on the first 5 characters (first5_char) that we send retreive all the exisiting hashed passwords

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #get the first 5 char and then 5 till end
    first5_char, tail = sha1password[:5], sha1password[5:] 
    res = request_api_data(first5_char)
    return get_password_leaks_count(res,tail)

#based on the given arguments/passwords,  if found print the number of times the password has been leaked ! 
def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!' 

    
#call it from cmd... its [1:] because the first argument[0:] is always the name of the file itself
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))