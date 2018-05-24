#!/usr/bin/env python
# vim: fdm=indent
'''
author:     Fabio Zanini
date:       15/08/17
content:    Test CountsTable class.
'''
# Script
if __name__ == '__main__':

    # NOTE: an env variable for the config file needs to be set when
    # calling this script
    from singlet.counts_table_sparse import CountsTableSparse
    ct = CountsTableSparse.from_tablename('example_PBMC_sparse')

    #print('Test statistics of CountsTable')
    #assert(ct.get_statistics(metrics=('min', 'cv')).iloc[0, 0] == 29.0)
    #print('Done!')

    print('Test normalization of CountsTable')
    ctn = ct.iloc[-200:]
    ctn = ctn.normalize('counts_per_million')
    assert(int(ctn.iloc[-2, -1]) == 17070)
    print('Done!')
