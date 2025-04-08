import pandas as pd
import numpy as np

if __name__ == "__main__":
    df = pd.read_csv("data/24250201.csv")
    
    for subject in df.keys():
        if subject in ['语文', '数学', '英语']:
            # 计算参考人数
            count = df[subject].count()
            # 计算平均分
            avg_score = df[subject].mean()
            # 计算标准差
            std_score = df[subject].std()
            # 计算最高分
            max_score = df[subject].max()
            # 计算最低分
            min_score = df[subject].min()

            # 分层统计
            # 计算优秀人数
            excellent_count = (df[subject] >= 90).sum()
            # 计算良好人数
            good_count = ((df[subject] >= 75) & (df[subject] < 90)).sum()
            # 计算及格人数
            pass_count = ((df[subject] >= 60) & (df[subject] < 75)).sum()
            # 计算不及格人数
            fail_count = (df[subject] < 60).sum()

            # 计算优秀率
            excellent_rate = (excellent_count / count) * 100
            # 计算良好率
            good_rate = (good_count / count) * 100
            # 计算及格率
            pass_rate = (pass_count / count) * 100
            # 计算不及格率
            fail_rate = (fail_count / count) * 100
            
            print(f"Subject: {subject}")
            print(f"参考人数: {count}")
            print(f"平均分: {avg_score:.2f}")
            print(f"标准差: {std_score:.2f}")
            print(f"最高分: {max_score}")
            print(f"最低分: {min_score}")
            print(f"优秀人数: {excellent_count}")
            print(f"良好人数: {good_count}")
            print(f"及格人数: {pass_count}")
            print(f"不及格人数: {fail_count}")
            print(f"优秀率: {excellent_rate:.2f}%")
            print(f"良好率: {good_rate:.2f}%")
            print(f"及格率: {pass_rate:.2f}%")
            print(f"不及格率: {fail_rate:.2f}%")
            print("-" * 40)