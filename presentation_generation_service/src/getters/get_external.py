import os
from constants import EXTERNAL_BUCKET_NAME, FILE_PROCESSORS, S3_CLIENT
import matplotlib.pyplot as plt
from uuid import uuid4


def get_external(fn: str):
    S3_CLIENT.download_file(EXTERNAL_BUCKET_NAME, fn, fn)
    d = fn.split('.')[-1]
    # if d.shape[0] > d.shape[1]:
    #     d = d.T
    df = FILE_PROCESSORS[d](fn)
    ds = []
    print(df)
    os.remove(fn)
    for ci in df.columns:
        print(ci, df[ci].dtype)
        if df[ci].dtype==float:
            plt.plot(df[ci])
            plt.title(ci)
        else:
            counts = df[ci].value_counts()
            print(counts)
            if len(counts) < 5:
                plt.pie(counts, labels=counts)
            else:
                plt.bar(counts.index, counts.values)
        d = f'{str(uuid4())}.png'
        ds.append(d)
        plt.savefig(d)
        S3_CLIENT   
        plt.clf()
        os.remove(d)
    return d

