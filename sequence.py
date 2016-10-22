class sequence(object):
    def __init__(self, seq):
        self.UNIT_TYPE = ['个',
                          '万',
                          '亿',
                          '兆',
                          '京',
                          '垓',
                          '秭',
                          '穰',
                          '沟',
                          '涧',
                          '正',
                          '载',
                          '级',
                          '恒河沙',
                          '阿僧示氏',
                          '那由他'
                          ]
        self.NUM2CN = {
            "0": "零",
            "1": "一",
            "2": "二",
            "3": "三",
            "4": "四",
            "5": "五",
            "6": "六",
            "7": "七",
            "8": "八",
            "9": "九"
        }
        self.WEIGH_TYPE = ["占", "十", "百", "千"]
        self.GROUP_LEN = len(self.WEIGH_TYPE)
        self.UNKNOW = "?"

        self.trans2cn = self.trans_seq(seq)

    def divide_seq(self, seq):
        group_arr = []
        seq = str(seq)
        seq_len = len(seq)
        group_len, remain = divmod(seq_len, self.GROUP_LEN)

        if seq[:remain]:
            group_arr.append(seq[:remain])
            seq = seq[remain:]

        for group_index in range(group_len):
            group_arr.append(seq[:self.GROUP_LEN])
            seq = seq[self.GROUP_LEN:]

        return group_arr[::-1]

    def trans_block(self, block_seq, unit):
        tmp_arr = []
        for index, num in enumerate(block_seq[::-1]):
            if (num == '0'):
                one_cn = "零"
            else:
                one_cn = self.NUM2CN[num] + self.WEIGH_TYPE[index]
            tmp_arr.append(one_cn)

        for index, one_cn in enumerate(tmp_arr):
            if one_cn != '零':
                tmp_arr[index] = tmp_arr[index] + unit
                break

        tmp_arr = tmp_arr[::-1]
        tmp_seq = "".join(tmp_arr)
        return self.clean_seq(tmp_seq)

    def clean_seq(self, tmp_seq):
        import re
        tmp_seq = re.sub("零+", "零", tmp_seq)
        tmp_seq = re.sub("零$", "", tmp_seq)
        tmp_seq = re.sub("占", "", tmp_seq)
        tmp_seq = re.sub("个", "", tmp_seq)
        return tmp_seq

    def localize(self, tmp_seq):
        import re
        if len(tmp_seq) <= 3:
            tmp_seq = re.sub("一十", "十", tmp_seq)
        return tmp_seq

    def trans_seq(self, seq):
        if not seq:
            return "输入错误"
        group_res = []
        group_arr = self.divide_seq(seq)

        for index, block_seq in enumerate(group_arr):
            try:
                unit = self.UNIT_TYPE[index]
            except IndexError:
                unit = self.UNKNOW
            transed_block = self.trans_block(block_seq, unit)
            group_res.append(transed_block)

        trans_seq = self.clean_seq("".join(group_res[::-1]))
        trans_seq = self.localize(trans_seq)
        return trans_seq


if __name__ == "__main__":
    test_arr = [2,
                20,
                102,
                1012,
                1004,
                50000000,
                900000000,
                1021234124435425235,
                112838929922323300000000006]
    for test_num in test_arr:
        print(sequence(test_num).trans2cn)
