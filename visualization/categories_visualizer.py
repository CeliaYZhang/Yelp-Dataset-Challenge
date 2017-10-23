# Parse and visualize the categories that the businesses fall into. 

import matplotlib.pyplot as plt
import numpy as np
import operator

def countCategories(df):
    cat_count = {}
    for cats in df['categories']:
        for c in cats:
            if c in cat_count:
                cat_count[c] += 1
            else:
                cat_count[c] = 1
    return cat_count

def topNCategories(df, n):
    cat_count = countCategories(df)
    sorted_count = sorted(cat_count.items(), key=operator.itemgetter(1))
    sorted_count.reverse()
    return sorted_count[:n]

def topNCategoriesBarGraph(df, n, fname):
    """ Create bar graph of top n most represented categories. """
    counts = topNCategories(df, n)
    cats, nstores = zip(*counts)
    y_pos = np.arange(n)
    fig = plt.figure()
    plt.bar(y_pos, nstores, align='center', alpha=0.5)
    plt.xticks(y_pos, cats, rotation=45)
    plt.xlabel('Category')
    plt.ylabel('Number of Businesses In Category')
    plt.title(str(n) + ' Most Popular Business Categories')
    plt.tight_layout()
    plt.show()
    fig.savefig(fname)
    
def culturalCategoriesBarGraph(df, fname):
    """ Create bar graph of cultural categories and their business counts. """
    counts = countCategories(df)
    cultures = ['American (Traditional)', 'American (New)', 'Mexican', 'Chinese', 'Japanese']
    y_pos = np.arange(len(cultures))
    nstores = [counts[c] for c in cultures]
    fig = plt.figure()
    plt.bar(y_pos, nstores, align='center', alpha=0.5)
    plt.xticks(y_pos, cultures, rotation=45)
    plt.xlabel('Culture')
    plt.ylabel('Number of Businesses In Category')
    plt.title('Number of Businesses in Cultural Categories')
    plt.tight_layout()
    plt.show()
    fig.savefig(fname)    