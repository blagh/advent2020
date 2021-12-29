from dataclasses import dataclass, field
from math import log2
from functools import reduce

@dataclass
class LiteralPacket:
    version: int
    type_id: int

    # literal data
    data: str = field(default="")
    int_data: int = field(default=None)

    def add_literal_data(self, chars):
        self.data += chars
        self.int_data = int(self.data, 2)

    def version_sum(self):
        return self.version

    def value(self):
        return self.int_data

@dataclass
class OperatorPacket:
    version: int
    type_id: int

    # operator data
    length_type_id: int = field(default=None)
    sub_packets: list[int] = field(default_factory=list)

    def add_length_type_id(self, chars):
        self.length_type_id = int(chars, 2)

    def add_sub_packets(self, chars):
        print("parsing for sub packets", chars)

        x = 0
        while x < len(chars):
            sub_packet, packet_len = parse(chars[x:])

            x += packet_len

            self.sub_packets.append(sub_packet)

    def version_sum(self):
        sum = self.version
        for p in self.sub_packets:
            sum += p.version_sum()

        return sum

    def value(self):
        sub_values = [p.value() for p in self.sub_packets]

        if self.type_id == 0: #sum
            return sum(sub_values)
        elif self.type_id == 1: #product
            return reduce(lambda a, b: a*b, sub_values)
        elif self.type_id == 2: #minimum
            return min(sub_values)
        elif self.type_id == 3: #maximum
            return max(sub_values)
        elif self.type_id == 5: #greater_than
            return 1 if sub_values[0] > sub_values[1] else 0
        elif self.type_id == 6: #less_than
            return 1 if sub_values[0] < sub_values[1] else 0
        elif self.type_id == 7: #equal_to
            return 1 if sub_values[0] == sub_values[1] else 0

def convert_to_binary(input):
    length = len(input) * log2(16)
    input = bin(int(input, 16))[2:].zfill(int(length))
    # print(input)

    return input

def parse(input):
    x = 0

    # print(input)

    current_packet = None

    print(x, len(input), input[x:])

    if int(input[x:]) == 0:
        return

    version = int(input[x:x+3], 2)
    type_id = int(input[x+3:x+6], 2)

    print("version: ", version)
    print("type_id: ", type_id)

    x += 6
    if type_id == 4:
        current_packet = LiteralPacket(version, type_id)

        while True:
            start_x = x

            current_packet.add_literal_data(input[x+1:x+5])

            x += 5
            if input[start_x] == "0": # this was the last bit
                break

    else:
        current_packet = OperatorPacket(version, type_id)
        current_packet.add_length_type_id(input[x])

        print("  operator", input[x])

        x += 1
        if current_packet.length_type_id == 0:

            sub_packet_len = int(input[x:x+15], 2)
            print("  len: ", input[x:x+15], sub_packet_len)

            x += 15

            print(input[x:x+sub_packet_len])
            current_packet.add_sub_packets(input[x:x+sub_packet_len])

            x += sub_packet_len
        elif current_packet.length_type_id == 1:

            sub_packet_count = int(input[x:x+11], 2)
            print("  count: ", input[x:x+11], sub_packet_count)

            x += 11
            for i in range(sub_packet_count):
                sub_packet, packet_len = parse(input[x:])

                x += packet_len

                current_packet.sub_packets.append(sub_packet)

        else:
            raise "problems!"

    print(current_packet, x)
    return current_packet, x

test_input = 'D2FE28'
print(test_input)
packets = parse(convert_to_binary(test_input))

print(packets)
assert(packets[0].int_data == 2021)

test_input = '38006F45291200'
print("---")
print(test_input)
packets = parse(convert_to_binary(test_input))
print(packets)
assert(packets[0].sub_packets[0].int_data == 10)
assert(packets[0].sub_packets[1].int_data == 20)

test_input = 'EE00D40C823060'
print("---")
print(test_input)
packets = parse(convert_to_binary(test_input))
print(packets)
assert(packets[0].sub_packets[0].int_data == 1)
assert(packets[0].sub_packets[1].int_data == 2)
assert(packets[0].sub_packets[2].int_data == 3)

def sum_versions(packets):
    sum = 0
    for p in packets:
        sum += p.version_sum()

    return sum

def test_this_input(input, expected_sum):
    print("---")
    print(input)
    packet, x = parse(convert_to_binary(input))
    print(input)
    print(packet)
    print(packet.version_sum())
    assert(packet.version_sum() == expected_sum)

test_this_input('8A004A801A8002F478', 16)
test_this_input('620080001611562C8802118E34', 12)
test_this_input('C0015000016115A2E0802F182340', 23)
test_this_input('A0016C880162017C3686B18A3D4780', 31)

def test_this_math(input, expected_value):
    print("---")
    print(input)
    packet, x = parse(convert_to_binary(input))
    print(input)
    print(packet)
    print(packet.value())
    assert(packet.value() == expected_value)

test_this_math("C200B40A82", 3)
test_this_math("04005AC33890", 54)
test_this_math("880086C3E88112", 7)
test_this_math("CE00C43D881120", 9)
test_this_math("D8005AC2A8F0", 1)
test_this_math("F600BC2D8F", 0)
test_this_math("9C005AC2F8F0", 0)
test_this_math("9C0141080250320F1802104A08", 1)


input = "A20D6CE8F00033925A95338B6549C0149E3398DE75817200992531E25F005A18C8C8C0001849FDD43629C293004B001059363936796973BF3699CFF4C6C0068C9D72A1231C339802519F001029C2B9C29700B2573962930298B6B524893ABCCEC2BCD681CC010D005E104EFC7246F5EE7328C22C8400424C2538039239F720E3339940263A98029600A80021B1FE34C69100760B41C86D290A8E180256009C9639896A66533E459148200D5AC0149D4E9AACEF0F66B42696194031F000BCE7002D80A8D60277DC00B20227C807E8001CE0C00A7002DC00F300208044E000E69C00B000974C00C1003DC0089B90C1006F5E009CFC87E7E43F3FBADE77BE14C8032C9350D005662754F9BDFA32D881004B12B1964D7000B689B03254564414C016B004A6D3A6BD0DC61E2C95C6E798EA8A4600B5006EC0008542D8690B80010D89F1461B4F535296B6B305A7A4264029580021D1122146900043A0EC7884200085C598CF064C0129CFD8868024592FEE9D7692FEE9D735009E6BBECE0826842730CD250EEA49AA00C4F4B9C9D36D925195A52C4C362EB8043359AE221733DB4B14D9DCE6636ECE48132E040182D802F30AF22F131087EDD9A20804D27BEFF3FD16C8F53A5B599F4866A78D7898C0139418D00424EBB459915200C0BC01098B527C99F4EB54CF0450014A95863BDD3508038600F44C8B90A0801098F91463D1803D07634433200AB68015299EBF4CF5F27F05C600DCEBCCE3A48BC1008B1801AA0803F0CA1AC6200043A2C4558A710E364CC2D14920041E7C9A7040402E987492DE5327CF66A6A93F8CFB4BE60096006E20008543A8330780010E8931C20DCF4BFF13000A424711C4FB32999EE33351500A66E8492F185AB32091F1841C91BE2FDC53C4E80120C8C67EA7734D2448891804B2819245334372CBB0F080480E00D4C0010E82F102360803B1FA2146D963C300BA696A694A501E589A6C80"

input = convert_to_binary(input)
packet, x = parse(input)
print(packet.value())
