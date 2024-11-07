import math
from eth2spec.deneb import mainnet as spec

# BN_FR_MODULUS = 21888242871839275222246405745257275088548364400416034343698204186575808495617
BN_FQ_MODULUS = 21888242871839275222246405745257275088696311157297823662689037894645226208583

def int_to_limbs(number, limb_size=15, num_limbs=3):
    # Ensure the number fits within 255 bits
    # assert number <= (1 << 255), "Number must be less than 2^255"
    
    # Convert number to a byte array (32 bytes to cover 255 bits)
    byte_array = number.to_bytes(33, byteorder='little')

    # Extract limbs
    limbs = []
    for i in range(num_limbs):
        start_index = i * limb_size
        end_index = start_index + limb_size
        if i == num_limbs - 1:
            # For the last limb, ensure it has 15 bytes
            limb_bytes = byte_array[start_index:end_index] #.ljust(field_size, b'\x00')
        else:
            limb_bytes = byte_array[start_index:end_index]
        limbs.append(limb_bytes)

    # Convert each limb to a big-endian hex string
    limbs_hex = [limb[::-1].hex() for limb in limbs]

    return limbs_hex

def format_limbs_as_string(limbs):
    return "[ 0x" + ", 0x".join(limbs) + " ]"

def number_to_noir_bigint(n: int, limb_size=15, num_limbs=3):
    return format_limbs_as_string(int_to_limbs(n, limb_size, num_limbs))

def redc(modulus):
    # redc = floor(2^2k / p)
    # k = floor(log_2(modulus)) + 1
    k = math.floor(math.log2(modulus)) + 1
    print("k", k)
    return math.floor((2 ** (2 * k)) // modulus)

def bls_fr_redc():
    return redc(spec.BLS_MODULUS)

def bn_fq_redc():
    return redc(BN_FQ_MODULUS)

def format_roots_of_unity(roots):
    formatted_roots = [number_to_noir_bigint(root) for root in roots]
    # print("[ BigNum { limbs: " + " } ,\n BigNum { limbs: ".join(formatted_roots) + " } ]")
    # The formatting that was used in v1 of the blobs circuit:
    # print_to_file("roots.txt", "[ BigNum { limbs: " + " } ,\n BigNum { limbs: ".join(formatted_roots) + " } ]")
    print_to_file("roots.txt", "[ BigNum { limbs: " + " } ,\n BigNum { limbs: ".join(formatted_roots) + " } ]")


def print_roots_of_unity(msg, roots):
    print(msg)
    format_roots_of_unity(roots)

def compute_roots_of_unity():
    roots = spec.bit_reversal_permutation(spec.compute_roots_of_unity(spec.FIELD_ELEMENTS_PER_BLOB))
    print_roots_of_unity("\nroots:", roots)

def compute_negative_roots_of_unity():
    roots = spec.bit_reversal_permutation(spec.compute_roots_of_unity(spec.FIELD_ELEMENTS_PER_BLOB))
    negative_roots = [spec.BLS_MODULUS - root for root in roots]
    print_roots_of_unity("\nnegative roots:", negative_roots)

def compute_simple_roots_of_unity():
    FIELD_ELEMENTS_PER_SIMPLE_BLOB = 8
    simple_roots = spec.bit_reversal_permutation(spec.compute_roots_of_unity(FIELD_ELEMENTS_PER_SIMPLE_BLOB))
    print_roots_of_unity("\nsimple roots:", simple_roots)
    
def print_int_3_formats(msg, n: int):
    print(f"{msg}", n)
    print(f"{msg}", n.to_bytes(33, 'big').hex())
    print(f"{msg}", number_to_noir_bigint(n))
    print("\n")

def print_to_file(filename, content):
    # Open the file in write mode and write the content
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Content written to {filename}")



def setup():
    # compute_simple_roots_of_unity()

    compute_roots_of_unity()
    # compute_negative_roots_of_unity()

    # print_int_3_formats("bls modulus:", spec.BLS_MODULUS)

    # DOUBLE_MODULUS = 2 * spec.BLS_MODULUS
    # print_int_3_formats("double modulus:", DOUBLE_MODULUS)

    # print_int_3_formats("bn fq modulus:", BN_FQ_MODULUS)

    # print_int_3_formats("bls redc:", bls_fr_redc())

    # print_int_3_formats("bn redc:", bn_fq_redc())








def compute_mike_blob_proof():
    roots_of_unity = spec.bit_reversal_permutation(spec.compute_roots_of_unity(spec.FIELD_ELEMENTS_PER_BLOB))

    # x0 = roots_of_unity[0] # this is the number 1
    # x1 = roots_of_unity[1]
    z = 2

    blob = get_mike_blob()
    # print("BLOB", blob)
    commitment = spec.blob_to_kzg_commitment(blob)
    polynomial = spec.blob_to_polynomial(blob)

    # proof0, y0 = spec.compute_kzg_proof_impl(polynomial, x0)
    # proof1, y1 = spec.compute_kzg_proof_impl(polynomial, x1)
    proof, y = spec.compute_kzg_proof_impl(polynomial, z)

    # print("y0", y0)
    # print("y1", y1)
    print_int_3_formats("y:", y)


# def field_arith():
#     x = spec.BLSFieldElement(spec.BLS_MODULUS - 1)
#     z = x * x
#     print(x)

def get_mike_blob():
    # FIELD_ELEMENTS_PER_BLOB = 8
    values = [
        0
        for _ in range(spec.FIELD_ELEMENTS_PER_BLOB)
    ]

    # print("VALUES", values)

    values[0] = 0x1234
    values[1] = 0xabcd
    values[2] = 0x69

    b = bytes()
    for v in values:
        b += v.to_bytes(32, spec.KZG_ENDIANNESS)

    return spec.Blob(b)

def int_to_hex(n, bytes=32):
    return n.to_bytes(bytes, 'big').hex()

def big_add():
    max = 2 ** 64
    print("max:", max)
    a = 21888242871839275222246405745257275088548364400416034343698204186575808495617
    a_hex = int_to_hex(a, 32)
    a_noir = number_to_noir_bigint(a, 4, 8)
    print("a:", a)
    print("a_hex:", a_hex)
    print("a_noir:", a_noir)
    # a0 = a % max
    # a1 = (a // max) % max
    # print("a:", a)
    # print("a_hex:", a_hex)
    # print("a0:", int_to_hex(a0, 12))
    # print("a1:", int_to_hex(a1, 12))
    # out = a + a
    # out0 = out % max
    # print("out0:", int_to_hex(out0, 12))
    # out1 = (out // max) % max
    # print("out1:", int_to_hex(out1, 12))
    # out2 = ((out // max) // max) % max
    # print("out2:", int_to_hex(out2, 12))
    # print(int_to_hex(out, 513))
    # outn = (out >> 4096) % max
    # print(int_to_hex(outn, 12))


def main():
    print("HI MUM!!!! I'm doing python!!!\n\n")

    # compute_mike_blob_proof()

    # big_add()

    # field_arith()

    setup()

main()