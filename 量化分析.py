import pandas as pd 
from pandas import Series, DataFrame 
import numpy as np
import statsmodels.api as sm 
import scipy.stats as scs 
import matplotlib.pyplot as plt
factors = ['B/M','EPS','PEG','ROE','ROA','GP/R','P/R','L/A','FAP','CMV']
#月初取出因子数值
def get_factors(fdate,factors):
    stock_set = get_index_stocks('000001.XSHG',fdate)
    q = query(
        valuation.code,
        balance.total_owner_equities/valuation.market_cap/100000000,
        income.basic_eps,
        valuation.pe_ratio,
        income.net_profit/balance.total_owner_equities,
        income.net_profit/balance.total_assets,
        income.total_profit/income.operating_revenue,
        income.net_profit/income.operating_revenue,
        balance.total_liability/balance.total_assets,
        balance.fixed_assets/balance.total_assets,
        valuation.circulating_market_cap
        ).filter(
        valuation.code.in_(stock_set),
        valuation.circulating_market_cap
    )
    fdf = get_fundamentals(q, date=fdate)
    fdf.index = fdf['code']
    fdf.columns = ['code'] + factors
    return fdf.iloc[:,-10:]
fdf = get_factors('2015-01-01',factors)
fdf.head()
#排序：

score = fdf['B/M'].order()
score.head()
#模型构建：

def score_stock(fdate):
    #CMV，FAP,PEG三个因子越小收益越大,分值越大，应降序排；B/M，P/R越大收益越大应顺序排
    effective_factors = {'B/M':True,'PEG':False,'P/R':True,'FAP':False,'CMV':False}
    fdf = get_factors(fdate)
    score = {}
    for fac,value in effective_factors.items():
        score[fac] = fdf[fac].rank(ascending = value,method = 'first')
    print DataFrame(score).T.sum().order(ascending = False).head(5)）
    score_stock = list(DataFrame(score).T.sum().order(ascending = False).index)
    return score_stock,fdf['CMV']

def get_factors(fdate):
    factors = ['B/M','PEG','P/R','FAP','CMV']
    stock_set = get_index_stocks('000001.XSHG',fdate)
    q = query(
        valuation.code,
        balance.total_owner_equities/valuation.market_cap/100000000,
        valuation.pe_ratio,
        income.net_profit/income.operating_revenue,
        balance.ffixed_assets/balance.total_assets,
        valuation.circulating_market_cap
        ).filter(
        valuation.code.in_(stock_set)
    )
    fdf = get_fundamentals(q,date = fdate)
    fdf.index = fdf['code']
    fdf.columns = ['code'] + factors
    return fdf.iloc[:,-5:]
[score_result,CMV] = score_stock('2016-01-01')
year = ['2009','2010','2011','2012','2013','2014','2015']
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
factors = ['B/M','PEG','P/R','FAP','CMV']
result = {}

for i in range(7*12):
    startdate = year[i/12] + '-' + month[i%12] + '-01'
    try:
        enddate = year[(i+1)/12] + '-' + month[(i+1)%12] + '-01'
    except IndexError:
        enddate = '2016-01-01'
    try:
        nextdate = year[(i+2)/12] + '-' + month[(i+2)%12] + '-01'
    except IndexError:
        if enddate == '2016-01-01':
            nextdate = '2016-02-01'
        else:
            nextdate = '2016-01-01'
    print 'time %s'%startdate
    #综合5个因子打分后，划分几个组合
    df = DataFrame(np.zeros(7),index = ['Top20','port1','port2','port3','port4','port5','benchmark'])
    [score,CMV] = score_stock(startdate)
    port0 = score[:20]
    port1 = score[: len(score)/5]
    port2 = score[ len(score)/5+1: 2*len(score)/5]
    port3 = score[ 2*len(score)/5+1: -2*len(score)/5]
    port4 = score[ -2*len(score)/5+1: -len(score)/5]
    port5 = score[ -len(score)/5+1: ]
    print len(score)
    df.ix['Top20'] = caculate_port_monthly_return(port1,startdate,enddate,nextdate,CMV)
    df.ix['port1'] = 
caculate_port_monthly_return(port1,startdate,enddate,nextdate,CMV)
    df.ix['port2'] = caculate_port_monthly_return(port2,startdate,enddate,nextdate,CMV)
    df.ix['port3'] = caculate_port_monthly_return(port3,startdate,enddate,nextdate,CMV)
    df.ix['port4'] = caculate_port_monthly_return(port4,startdate,enddate,nextdate,CMV)
    df.ix['port5'] = caculate_port_monthly_return(port5,startdate,enddate,nextdate,CMV)
    df.ix['benchmark'] = caculate_benchmark_monthly_return(startdate,enddate,nextdate)
    result[i+1]=df
backtest_results = pd.DataFrame(result)
