class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return 'Zero'

        ones_map={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",
        7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",
        12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",
        16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}

        tens_map= {20:"Twenty",30:"Thirty",40:"Forty",
        50:"Fifty",60:"Sixty",70:"Seventy",
        80:"Eighty",90:"Ninety"} 

        def getString(n):
            res = []
            hundreds = n // 100
            if hundreds:
                res.append(ones_map[hundreds] + " Hundred")
            last_2 = n % 100
            if last_2 >= 20:
                tens, ones = last_2 // 10, last_2 % 10
                res.append(tens_map[tens * 10])
                if ones:
                    res.append(ones_map[ones])
            elif last_2:
                res.append(ones_map[last_2])

            return " ".join(res) 

        postfix=[""," Thousand", " Million", " Billion"]
        i=0
        res=[]
        while num:
            digits = num % 1000
            s = getString(digits)
            if s:
                res.append(s + postfix[i])
            num = num // 1000
            i += 1
        res.reverse()
        
        return " ".join(res)


# num = 1000007
# i=0, while num: yes,
#               digits = 1000007 % 1000 = 007
#               s = getString(007) => res=[], hundreds=007//100=0,
#                   last_2=007%100=7, res=['Seven']
#               postfix[0] = '', res = ['Seven'],
#               num = 1000007//1000 = 1000, i=1
#
# i=1, while num: yes,
#               digits = 1000 % 1000 = 000
#               s = getString(000) => res=[], hundreds=000//100=0,
#                   last_2=000%100=0, res=[]
#               return " ".join([]) = ''
#               if s: False, so res remains ['Seven']
#               num = 1000//1000 = 1, i=2
#
# i=2, while num: yes,
#               digits = 1 % 1000 = 001
#               s = getString(001) => res=[], hundreds=001//100=0,
#                   last_2=001%100=1, res=['One']
#               postfix[2] = ' Million',
#               res = ['Seven', 'One Million']
#               num = 1//1000 = 0, i=3
#
# while num: no, because num=0
#
# res.reverse()
# res = ['One Million', 'Seven']
#
# return " ".join(res)
# Output: "One Million Seven"