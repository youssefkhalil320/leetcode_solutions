class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isValid_Ipv4(ip: str) -> bool:
            if ip == "":
                return False

            ipstr = ip.split('.')

            if len(ipstr) != 4:
                return False

            for num in ipstr:
                if num == "" or (num[0] == "0" and len(num) > 1):
                    return False
                if num.isdigit():
                    if int(num) < 0 or int(num) > 255:
                        return False
                else:
                    return False

            return True

        def isValid_Ipv6(ip: str) -> bool:
            counter = 0
            ipstr = ip.split(":")
            if len(ipstr) != 8:
                return False

            for num in ipstr:
                if num == "" or len(num) > 4:
                    return False
                for letter in num:
                    if letter.isalpha() and letter not in "abcdefABCDEF":
                        return False
            return True

        if isValid_Ipv4(queryIP):
            return "IPv4"
        if isValid_Ipv6(queryIP):
            return "IPv6"
        return "Neither"
