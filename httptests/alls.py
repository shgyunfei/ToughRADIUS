#!/usr/bin/env python
#coding:utf-8

import bas_test
import node_test 
import product_test
import member_test

if __name__ == '__main__':
    node_test.test_post_node()
    bas_test.test_post_bas()
    product_test.test_post_product()
    member_test.test_post_member()
    # member_test.test_post_member_100()