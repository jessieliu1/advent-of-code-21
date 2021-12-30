from util.util import file_to_string_list
import sys

def hex_to_bin(hex_val):
    h_size = len(hex_val) * 4
    int_value = int(hex_val, base=16)
    return str(bin(int_value))[2:].zfill(h_size)

def read_packets(filename):
    hex = file_to_string_list(filename)[0]
    packet = hex_to_bin(hex)
    version, next_idx = parse_packet(packet, 0)
    return version

def read_packets_from_str(str):
    packet = hex_to_bin(str.strip())
    val, _ = parse_packet(packet, 0)
    return val

def parse_packet(packet, start_idx):
    if len(packet[start_idx:]) < 11:
        return -1, len(packet)
    next_idx = 0
    type = get_packet_type(packet, start_idx)
    old_val = None
    if type == 4:
        literal, next_idx = get_literal_number(packet, start_idx)
        return literal, next_idx
    else:
        if packet[start_idx+6] == "0":
            sub_length = get_subpacket_length(packet, start_idx)
            subpacket_start = start_idx + 22
            next_idx = subpacket_start
            while next_idx < subpacket_start + sub_length:
                new_val, next_idx = parse_packet(packet, next_idx)
                if new_val < 0:
                    break
                if old_val == None:
                    old_val = new_val
                else:
                    old_val = operation(type, old_val, new_val)
            return old_val, next_idx
        else:
            sub_num = get_subpacket_num(packet, start_idx)
            subpacket_start = start_idx + 18
            next_idx = subpacket_start
            num_packets = 0
            while num_packets < sub_num:
                new_val, next_idx = parse_packet(packet, next_idx)
                if new_val < 0:
                    break
                if old_val == None:
                    old_val = new_val
                else:
                    old_val = operation(type, old_val, new_val)
                num_packets += 1
            return old_val, next_idx

def operation(type, old_val, new_val):
    match type:
        case 0:
            return old_val + new_val
        case 1:
            return old_val * new_val
        case 2:
            return min(old_val, new_val)
        case 3:
            return max(old_val, new_val)
        case 5:
            return 1 if old_val > new_val else 0
        case 6:
            return 1 if old_val < new_val else 0
        case 7:
            return 1 if old_val == new_val else 0

def parse_packet_version(packet, start_idx):
    if len(packet[start_idx:]) < 11:
        return 0, len(packet)
    next_idx = 0
    version = get_packet_version(packet, start_idx)
    type = get_packet_type(packet, start_idx)
    if type == 4:
        literal, next_idx = get_literal_number(packet, start_idx)
        return version, next_idx
    else:
        if packet[start_idx+6] == "0":
            sub_length = get_subpacket_length(packet, start_idx)
            subpacket_start = start_idx + 22
            next_idx = subpacket_start
            while next_idx < subpacket_start + sub_length:
                new_version, next_idx = parse_packet(packet, next_idx)
                version += new_version
            return version, next_idx
        else:
            sub_num = get_subpacket_num(packet, start_idx)
            subpacket_start = start_idx + 18
            next_idx = subpacket_start
            num_packets = 0
            while num_packets < sub_num:
                new_version, next_idx = parse_packet(packet, next_idx)
                version += new_version
                num_packets += 1
            return version, next_idx

def get_packet_version(packet, start_idx):
    version_bin = packet[start_idx:start_idx+3]
    return int(version_bin, 2)

def get_packet_type(packet, start_idx):
    type_bin = packet[start_idx+3:start_idx+6]
    return int(type_bin, 2)

def get_literal_number(packet, start_idx):
    literal = ""
    chunk_start = start_idx+6
    while True:
        chunk = packet[chunk_start:chunk_start+5]
        literal += chunk[1:]
        chunk_start += 5
        if chunk[0] == "0":
            break
    return int(literal, 2), chunk_start

def get_subpacket_length(packet, start_idx):
    return int(packet[start_idx+7:start_idx+22], 2)

def get_subpacket_num(packet, start_idx):
    return int(packet[start_idx+7:start_idx+18], 2)

def main():
    print(read_packets(sys.argv[1]))

main()
