str = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"

hex_to_dec = [int(str[i:i+2],16) for i in range(0,len(str),2)]

char_distribution = []
for key in range(1,10):
    count_char = [0]*256

    for char in hex_to_dec[::key]:
        count_char[char] +=1
    
    q_i = [(char/sum(count_char))**2 for char in count_char]
    char_distribution.append(sum(q_i))

key = char_distribution.index(max(char_distribution))+1
# key = 7

## Finding the key

def sort_acc_to_e(pos_e):
    possible = []
    while(max(pos_e)!=0):
        possible.append(pos_e.index(max(pos_e)))
        pos_e[pos_e.index(max(pos_e))] = 0
    return possible

keys = []
for i in range(0,7):
    char_at_i = hex_to_dec[i::key]
    key_char = []
    pos_e = [0]*256
    for xor_char in range (0,255):
        xored_char_at_i =  [xor_char^char for char in char_at_i]
        fraction_of_e = xored_char_at_i.count(101)/len(xored_char_at_i)

        if 32<=min(xored_char_at_i)<48 and 58<=max(xored_char_at_i)<=127 and fraction_of_e > 0.05 :
            pos_e[xor_char] = fraction_of_e
            key_char.append(xor_char)

    key_char = sort_acc_to_e(pos_e)
    #print(key_char)
    
keys = [186,31,145,178,83,205,62]

decryted_msg = []
s = ''
for i in range(len(hex_to_dec)):
    k = keys[i%key]^hex_to_dec[i]
    decryted_msg.append(k)
    s += chr(k)
print(s)
