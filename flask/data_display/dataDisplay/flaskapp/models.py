# -*- coding: utf-8 -*-
"""Data models"""

from dataDisplay.database import db


def init_databse(self, columns, data):
    """
    对应数据库模型类的初始化，值为每个行表中的所有值
    :param self:
    :param columns:
    :param data:
    :return:
    """
    for index in range(len(columns)):
        # 将缺省值做null处理
        if data[index]:
            value = data[index]
        else:
            value = ''

        print columns[index], ':', value
        setattr(self, columns[index], value)


class cop_ex_1(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    del_time = db.Column(db.TEXT)
    sp_time = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    p_head = db.Column(db.TEXT)
    co_country = db.Column(db.TEXT)
    na_fud = db.Column(db.TEXT)
    ks_mat = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_10(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    com_name = db.Column(db.TEXT)
    post_name = db.Column(db.TEXT)
    agr_per = db.Column(db.TEXT)
    tec_field = db.Column(db.TEXT)
    uni_name = db.Column(db.TEXT)
    exp_name = db.Column(db.TEXT)
    sex = db.Column(db.TEXT)
    age = db.Column(db.TEXT)
    aca_title = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    com_qua = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    re_time = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_11(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_name = db.Column(db.TEXT)
    p_field = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    co_area = db.Column(db.TEXT)
    co_com = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    eff_data = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    re_sit = db.Column(db.TEXT)
    cate = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_12(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    co_area = db.Column(db.TEXT)
    abo_par = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    re_fund = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_2(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    code = db.Column(db.TEXT)
    p_cat = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    jdel_com = db.Column(db.TEXT)
    uni = db.Column(db.TEXT)
    contacts = db.Column(db.TEXT)
    tel = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    del_time = db.Column(db.TEXT)
    ide_sit = db.Column(db.TEXT)
    pro_fud = db.Column(db.TEXT)
    pl_mate = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_3(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    sp_time = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    p_head = db.Column(db.TEXT)
    co_country = db.Column(db.TEXT)
    pro_fud = db.Column(db.TEXT)
    ks_mat = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    rec_time = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    rel = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_4(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    sp_time = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    co_country = db.Column(db.TEXT)
    sz_fund = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    tel = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_5(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    sp_time = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    co_country = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    tel = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_6(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_name = db.Column(db.TEXT)
    if_jp = db.Column(db.TEXT)
    reward = db.Column(db.TEXT)
    sta_time = db.Column(db.TEXT)
    exe_com = db.Column(db.TEXT)
    com_nat = db.Column(db.TEXT)
    co_com = db.Column(db.TEXT)
    uni_area = db.Column(db.TEXT)
    if_joint = db.Column(db.TEXT)
    industry = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_7(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    exe_com = db.Column(db.TEXT)
    com_nat = db.Column(db.TEXT)
    co_com = db.Column(db.TEXT)
    uni_area = db.Column(db.TEXT)
    if_leag = db.Column(db.TEXT)
    sta_time = db.Column(db.TEXT)
    re_time = db.Column(db.TEXT)
    re_fund = db.Column(db.TEXT)
    industry = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    area = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_8(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_name = db.Column(db.TEXT)
    sig_uni = db.Column(db.TEXT)
    faculty = db.Column(db.TEXT)
    pro_sub = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    sig_time = db.Column(db.TEXT)
    act_time = db.Column(db.TEXT)
    sup_mat = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class cop_ex_9(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    uni = db.Column(db.TEXT)
    major = db.Column(db.TEXT)
    cate = db.Column(db.TEXT)
    com_name = db.Column(db.TEXT)
    post_att = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    post_time = db.Column(db.TEXT)
    mun_fund = db.Column(db.TEXT)
    tow_mat = db.Column(db.TEXT)
    total = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_1(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    p_fud = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_10(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    p_fud = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)
    ex_time = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_11(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    p_fud = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)
    ex_time = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_12(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    p_fud = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_13(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    c_name = db.Column(db.TEXT)
    type = db.Column(db.TEXT)
    c_head = db.Column(db.TEXT)
    cont = db.Column(db.TEXT)
    tel = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    tow = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_2(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_cat = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    n_fud = db.Column(db.TEXT)
    ks_mate = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_3(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    p_fud = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_4(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    p_fud = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_5(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_cat = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    p_fud = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_6(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    p_fud = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_7(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    p_fud = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_8(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    p_fud = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class farm_socity_9(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    o_tow = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_1(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    kind_of_plan = db.Column(db.TEXT)
    project = db.Column(db.TEXT)
    classier = db.Column(db.TEXT)
    number = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_10(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    identity_time = db.Column(db.TEXT)
    certificate_num = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    incent_fund = db.Column(db.TEXT)
    order = db.Column(db.TEXT)
    econo_type = db.Column(db.TEXT)
    company_property = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_11(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    identity_time = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_12(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    plan_kind = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    kind = db.Column(db.TEXT)
    set_year = db.Column(db.TEXT)
    allocate_fund = db.Column(db.TEXT)
    under_com_acq_fund = db.Column(db.TEXT)
    kunshan_match = db.Column(db.TEXT)
    doc_num = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    pro_all_input = db.Column(db.TEXT)
    up_allcoate_fund = db.Column(db.TEXT)
    arrived_fund = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_13(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    area = db.Column(db.TEXT)
    all_num = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_14(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    plan_kind = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    kind = db.Column(db.TEXT)
    set_year = db.Column(db.TEXT)
    start_end_time = db.Column(db.TEXT)
    allocate_fund = db.Column(db.TEXT)
    under_com_acq_fund = db.Column(db.TEXT)
    year_allocate = db.Column(db.TEXT)
    local_match = db.Column(db.TEXT)
    self_raise = db.Column(db.TEXT)
    all_fund = db.Column(db.TEXT)
    arrived_fund = db.Column(db.TEXT)
    arr_fund_from2015 = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_15(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_16(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    up_allocate = db.Column(db.TEXT)
    kunshan_match = db.Column(db.TEXT)
    classier1 = db.Column(db.TEXT)
    classier2 = db.Column(db.TEXT)
    include_province_year = db.Column(db.TEXT)
    province_pro_num = db.Column(db.TEXT)
    start_end_time = db.Column(db.TEXT)
    include_nation_year = db.Column(db.TEXT)
    nation_pro_num = db.Column(db.TEXT)
    fovus_pro_settime = db.Column(db.TEXT)
    carry_time = db.Column(db.TEXT)
    all_input = db.Column(db.TEXT)
    self_raise = db.Column(db.TEXT)
    loan = db.Column(db.TEXT)
    state = db.Column(db.TEXT)
    annual_value = db.Column(db.TEXT)
    annual_pro_tax = db.Column(db.TEXT)
    annual_profit = db.Column(db.TEXT)
    accept = db.Column(db.TEXT)
    accept_year = db.Column(db.TEXT)
    conclusion = db.Column(db.TEXT)
    con_year = db.Column(db.TEXT)
    revoke = db.Column(db.TEXT)
    rev_year = db.Column(db.TEXT)
    rev_reason = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_17(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    identity_time = db.Column(db.TEXT)
    nation_iden_year = db.Column(db.TEXT)
    certificate_num = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    reward_fund = db.Column(db.TEXT)
    trade = db.Column(db.TEXT)
    technical_field = db.Column(db.TEXT)
    order = db.Column(db.TEXT)
    econo_type = db.Column(db.TEXT)
    com_property = db.Column(db.TEXT)
    nation_classer = db.Column(db.TEXT)
    double_dense = db.Column(db.TEXT)
    dense_iden_year = db.Column(db.TEXT)
    trade_kind = db.Column(db.TEXT)
    dense_com_num = db.Column(db.TEXT)
    province_revoke = db.Column(db.TEXT)
    nation_revoke = db.Column(db.TEXT)
    province_high_com = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_18(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_19(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    plan_kind = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    kind = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    set_year = db.Column(db.TEXT)
    allocate_fund = db.Column(db.TEXT)
    under_com_acq_fund = db.Column(db.TEXT)
    under_com_all_allo = db.Column(db.TEXT)
    local_match = db.Column(db.TEXT)
    self_raise = db.Column(db.TEXT)
    pro_all_fund = db.Column(db.TEXT)
    com_acq_fund = db.Column(db.TEXT)
    acq_fund_from2015 = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_2(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    super_pro_category = db.Column(db.TEXT)
    projec_tname = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    amount = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_20(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    kind = db.Column(db.TEXT)
    set_time = db.Column(db.TEXT)
    allocate_fund = db.Column(db.TEXT)
    under_con_acq_fund = db.Column(db.TEXT)
    kunshan_match = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    pro_all_input = db.Column(db.TEXT)
    up_allocate_amount = db.Column(db.TEXT)
    arrive_fund = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_21(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    all_num = db.Column(db.TEXT)
    area = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_22(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    identity_time = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    product_num = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    up_allocate = db.Column(db.TEXT)
    kunshan_match = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_23(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    all_num = db.Column(db.TEXT)
    year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_24(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    product_name = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    classer = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_25(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    company_property = db.Column(db.TEXT)
    naland_tax = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)
    reward_fund = db.Column(db.TEXT)
    certificate = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    pho = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_26(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    all_num = db.Column(db.TEXT)
    area = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_27(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_28(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_29(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    professor_tomn_name = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_3(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    classier = db.Column(db.TEXT)
    kind_of_paln = db.Column(db.TEXT)
    carrier_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_30(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)
    area = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_31(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    professor_tomn_name = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_32(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)
    area = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_33(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    manage_tax_insti = db.Column(db.TEXT)
    technical_field = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    area = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_34(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    sciencepark_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    identify = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_35(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    declare_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    set_year = db.Column(db.TEXT)
    up_reward_fund = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    pho = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_36(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    area = db.Column(db.TEXT)
    legal_num = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    mail_address = db.Column(db.TEXT)
    state = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_37(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    identify_yer = db.Column(db.TEXT)
    all_num = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_38(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pioneer_invest_name = db.Column(db.TEXT)
    kind = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_39(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    set_year = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    carry_time = db.Column(db.TEXT)
    all_invest = db.Column(db.TEXT)
    up_allocate = db.Column(db.TEXT)
    kunshan_match = db.Column(db.TEXT)
    accept = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    kind = db.Column(db.TEXT)
    fund_kind = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_4(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    pro_number = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_40(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    set_year = db.Column(db.TEXT)
    all_fund = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_41(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    area = db.Column(db.TEXT)
    all_num = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_42(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    certificate_num = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    order = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    fund_kind = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_43(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    all_num = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_44(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_contract_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    pro_fund = db.Column(db.TEXT)
    allocated = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_45(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    incubator_name = db.Column(db.TEXT)
    manage_com_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    operate_property = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_46(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    allocate = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_47(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    product_num = db.Column(db.TEXT)
    product_name = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    fund_kind = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_48(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    all_num = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_49(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    city_fund = db.Column(db.TEXT)
    town_fund = db.Column(db.TEXT)
    set_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_5(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    angel_invest_insti_pro = db.Column(db.TEXT)
    identify_proid = db.Column(db.TEXT)
    pro_id = db.Column(db.TEXT)
    invested_com_name = db.Column(db.TEXT)
    first_invest_amount = db.Column(db.TEXT)
    province_risk_amount = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_50(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    all_allocate = db.Column(db.TEXT)
    allocated = db.Column(db.TEXT)
    city_fund = db.Column(db.TEXT)
    town_fund = db.Column(db.TEXT)
    set_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_51(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    technical_filed = db.Column(db.TEXT)
    start_end_time = db.Column(db.TEXT)
    all_input = db.Column(db.TEXT)
    city_fund = db.Column(db.TEXT)
    reamrk = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_52(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    industry_name = db.Column(db.TEXT)
    belong_com_name = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_53(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    set_year = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    carry_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    reward_fund = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_54(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    city_fund = db.Column(db.TEXT)
    town_fund = db.Column(db.TEXT)
    set_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_55(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    pro_fund = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_56(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    incubator_name = db.Column(db.TEXT)
    manage_com_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    operate_property = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    yaer = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_57(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    order = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_58(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    indentify_year = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    classer = db.Column(db.TEXT)
    reward_fund = db.Column(db.TEXT)
    order = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_59(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    university_name = db.Column(db.TEXT)
    classer = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    bulid_year = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_6(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    pro_all_inveat = db.Column(db.TEXT)
    added_invest = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_60(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    fund_kind = db.Column(db.TEXT)
    company_property = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_61(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    not_pass_com = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_62(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    product_num = db.Column(db.TEXT)
    product_name = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    fund_kind = db.Column(db.TEXT)
    fund_kind2 = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    reward_fund = db.Column(db.TEXT)
    export = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    first_value = db.Column(db.TEXT)
    second_value = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_63(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pilot_name = db.Column(db.TEXT)
    manage_com_name = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_64(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    order = db.Column(db.TEXT)
    year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_65(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    fund_kind = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_66(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    set_year = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    carry_time = db.Column(db.TEXT)
    all_invest = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    kunshan_match = db.Column(db.TEXT)
    accept = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    state_track = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_67(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    area = db.Column(db.TEXT)
    all_num = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_68(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    start_end_time = db.Column(db.TEXT)
    province_fund = db.Column(db.TEXT)
    local_match = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_69(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    sart_end_time = db.Column(db.TEXT)
    all_invest = db.Column(db.TEXT)
    up_allocate = db.Column(db.TEXT)
    kunshan_match = db.Column(db.TEXT)
    pro_kind = db.Column(db.TEXT)
    accept = db.Column(db.TEXT)
    state_track = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_7(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    pro_content = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    company_property = db.Column(db.TEXT)
    local_manager = db.Column(db.TEXT)
    assistent_unit = db.Column(db.TEXT)
    start_end_time = db.Column(db.TEXT)
    self_raise = db.Column(db.TEXT)
    loan = db.Column(db.TEXT)
    putput_value = db.Column(db.TEXT)
    profit_tax = db.Column(db.TEXT)
    earning = db.Column(db.TEXT)
    apply_bank = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_70(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_71(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    certificate_num = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    trade = db.Column(db.TEXT)
    technical_filed = db.Column(db.TEXT)
    order = db.Column(db.TEXT)
    econo_kind = db.Column(db.TEXT)
    company_property = db.Column(db.TEXT)
    nation_class = db.Column(db.TEXT)
    nation_identify_year = db.Column(db.TEXT)
    double_dense = db.Column(db.TEXT)
    dense_iden_year = db.Column(db.TEXT)
    trade_kind = db.Column(db.TEXT)
    dense_com_num = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    province_revoke = db.Column(db.TEXT)
    nation_revoke = db.Column(db.TEXT)
    province_high_com = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_72(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    sciencepark_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    identify = db.Column(db.TEXT)
    year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_73(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    public_create_name = db.Column(db.TEXT)
    operate_name = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    identify_time = db.Column(db.TEXT)
    area = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_74(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    reward_fund = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_75(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    product_name = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    classer = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_76(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    product_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    identify_time = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    fund_kind = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_77(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    certificate_num = db.Column(db.TEXT)
    company_name = db.Column(db.TEXT)
    order = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    fund_kind = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_78(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    all_num = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_79(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    econo_kind = db.Column(db.TEXT)
    declare_year = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    review_state = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_8(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    kind = db.Column(db.TEXT)
    incubator_name = db.Column(db.TEXT)
    classier = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    company_property = db.Column(db.TEXT)
    local_manager = db.Column(db.TEXT)
    assistent_unit = db.Column(db.TEXT)
    start_end_time = db.Column(db.TEXT)
    self_raise = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_80(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    pro_num = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    pro_intro = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    start_end_time = db.Column(db.TEXT)
    all_fund = db.Column(db.TEXT)
    city_fund = db.Column(db.TEXT)
    allocated = db.Column(db.TEXT)
    local_match = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    state_track = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_81(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    allowance_kind = db.Column(db.TEXT)
    insti_name = db.Column(db.TEXT)
    operate_company = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)
    fund_amount = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    receipt_20170704 = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_82(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    basic_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    identify_year = db.Column(db.TEXT)
    reward_fund = db.Column(db.TEXT)
    basic_belong = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_83(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    funded = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_84(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    funded = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class high_new_tec_9(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    company_name = db.Column(db.TEXT)
    insti_num = db.Column(db.TEXT)
    tax_num = db.Column(db.TEXT)
    main_tax = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    econo_type = db.Column(db.TEXT)
    company_property = db.Column(db.TEXT)
    add = db.Column(db.TEXT)
    mold_enterprise = db.Column(db.TEXT)
    trade_kind = db.Column(db.TEXT)
    trade_name = db.Column(db.TEXT)
    trade_num = db.Column(db.TEXT)
    h_enter_num = db.Column(db.TEXT)
    identity_time = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class law_1(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    identify_year = db.Column(db.TEXT)
    nation_kind = db.Column(db.TEXT)
    province_kind = db.Column(db.TEXT)
    province_team = db.Column(db.TEXT)
    gusu_kind = db.Column(db.TEXT)
    gusu_team = db.Column(db.TEXT)
    kunshan_kind = db.Column(db.TEXT)
    kunshan_team = db.Column(db.TEXT)
    name = db.Column(db.TEXT)
    political_state = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    set_field = db.Column(db.TEXT)
    kind = db.Column(db.TEXT)
    up_allocate = db.Column(db.TEXT)
    local_match = db.Column(db.TEXT)
    house_subsidy = db.Column(db.TEXT)
    personal_phone = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    email = db.Column(db.TEXT)
    accept_view = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class patent_1(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    classer = db.Column(db.TEXT)
    plan_kind = db.Column(db.TEXT)
    pro_name = db.Column(db.TEXT)
    undertake_company = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    all_fund = db.Column(db.TEXT)
    doc_num = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_1(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_cate = db.Column(db.TEXT)
    p_subd = db.Column(db.TEXT)
    level = db.Column(db.TEXT)
    re_num = db.Column(db.TEXT)
    amount = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_10(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_name = db.Column(db.TEXT)
    yt_com = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    gra_dep = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_11(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    p_head = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    yt_uni = db.Column(db.TEXT)
    field = db.Column(db.TEXT)
    lx_year = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    p_input = db.Column(db.TEXT)
    new_input = db.Column(db.TEXT)
    pro_fund = db.Column(db.TEXT)
    wc_fund = db.Column(db.TEXT)
    yc_fund = db.Column(db.TEXT)
    loan_tx = db.Column(db.TEXT)
    h_fund = db.Column(db.TEXT)
    yb_tx = db.Column(db.TEXT)
    pro_dn_fund = db.Column(db.TEXT)
    pro_en_fund = db.Column(db.TEXT)
    ks_mat = db.Column(db.TEXT)
    fn_bk = db.Column(db.TEXT)
    ht_sale = db.Column(db.TEXT)
    ht_income = db.Column(db.TEXT)
    ht_profit = db.Column(db.TEXT)
    ht_ch = db.Column(db.TEXT)
    sj_sale = db.Column(db.TEXT)
    sj_input = db.Column(db.TEXT)
    fax = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_12(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    content = db.Column(db.TEXT)
    p_head = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    yt_uni = db.Column(db.TEXT)
    field = db.Column(db.TEXT)
    lx_year = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    p_fund = db.Column(db.TEXT)
    xd_fund = db.Column(db.TEXT)
    dn_fund = db.Column(db.TEXT)
    en_fund = db.Column(db.TEXT)
    ks_mat = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_13(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    yt_uni = db.Column(db.TEXT)
    field = db.Column(db.TEXT)
    lx_year = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    p_input = db.Column(db.TEXT)
    xd_fund = db.Column(db.TEXT)
    dn_fund = db.Column(db.TEXT)
    en_fund = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_14(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    com_na = db.Column(db.TEXT)
    input = db.Column(db.TEXT)
    y_input = db.Column(db.TEXT)
    n_input = db.Column(db.TEXT)
    xd_fund = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_15(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    cate = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    com_na = db.Column(db.TEXT)
    co_com = db.Column(db.TEXT)
    re_time = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    p_head = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    input = db.Column(db.TEXT)
    pro_fund = db.Column(db.TEXT)
    ks_mat = db.Column(db.TEXT)
    batch = db.Column(db.TEXT)
    pro_xd = db.Column(db.TEXT)
    ks_xd = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_16(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    cate = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    yt_com = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    con_per = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    p_head = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    sz_fund = db.Column(db.TEXT)
    ks_mat = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_17(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_cat = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    yt_com = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    s_fund = db.Column(db.TEXT)
    qz_fund = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_18(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    field = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    input = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    lx_sit = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    s_fund = db.Column(db.TEXT)
    qz_fund = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_19(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    lx_year = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    p_head = db.Column(db.TEXT)
    co_country = db.Column(db.TEXT)
    pro_fund = db.Column(db.TEXT)
    ks_mat = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_2(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    ach_name = db.Column(db.TEXT)
    win_com = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_20(db.Model):
    year = db.Column(db.INTEGER, primary_key=True)
    sat_num = db.Column(db.TEXT)
    income = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_21(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    lx_year = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    co_country = db.Column(db.TEXT)
    sz_fund = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_22(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    p_profile = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    lx_year = db.Column(db.TEXT)
    ss_time = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    co_country = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_23(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    com = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    re_fund = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_24(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_name = db.Column(db.TEXT)
    win_com = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_25(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    re_cat = db.Column(db.TEXT)
    com = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_26(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    re_cat = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    com = db.Column(db.TEXT)
    head = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    reward = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_27(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    re_name = db.Column(db.TEXT)
    re_com = db.Column(db.TEXT)
    head = db.Column(db.TEXT)
    sj_com = db.Column(db.TEXT)
    level = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    area = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_28(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    head = db.Column(db.TEXT)
    com = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    level = db.Column(db.TEXT)
    sz_reward = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_29(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    re_com = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    prof = db.Column(db.TEXT)
    field = db.Column(db.TEXT)
    level = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_3(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    sta_time = db.Column(db.TEXT)
    com_num = db.Column(db.TEXT)
    reins_num = db.Column(db.TEXT)
    con_rate = db.Column(db.TEXT)
    sta_l = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_30(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    re_name = db.Column(db.TEXT)
    re_com = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    head = db.Column(db.TEXT)
    sj_com = db.Column(db.TEXT)
    level = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    amount = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_31(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    re_name = db.Column(db.TEXT)
    re_com = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    head = db.Column(db.TEXT)
    sj_com = db.Column(db.TEXT)
    re_cat = db.Column(db.TEXT)
    level = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    amount = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_32(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    re_name = db.Column(db.TEXT)
    re_com = db.Column(db.TEXT)
    head = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    sj_com = db.Column(db.TEXT)
    level = db.Column(db.TEXT)
    year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_33(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    re_name = db.Column(db.TEXT)
    com = db.Column(db.TEXT)
    sj_com = db.Column(db.TEXT)
    level = db.Column(db.TEXT)
    cy_com = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_34(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    ss_name = db.Column(db.TEXT)
    del_com = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    re_sit = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_35(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_name = db.Column(db.TEXT)
    p_sit = db.Column(db.TEXT)
    inv_loc = db.Column(db.TEXT)
    fund_sor = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    kcen_name = db.Column(db.TEXT)
    field = db.Column(db.TEXT)
    dire = db.Column(db.TEXT)
    ksre_year = db.Column(db.TEXT)
    ks_fund = db.Column(db.TEXT)
    scen_name = db.Column(db.TEXT)
    szre_year = db.Column(db.TEXT)
    sz_fund = db.Column(db.TEXT)
    sjcen_name = db.Column(db.TEXT)
    sjre_year = db.Column(db.TEXT)
    sj_fund = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_36(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    c_com = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    aud_com = db.Column(db.TEXT)
    re_level = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    a_fund_1 = db.Column(db.TEXT)
    a_fund_2 = db.Column(db.TEXT)
    a_fund_3 = db.Column(db.TEXT)
    a_fund_4 = db.Column(db.TEXT)
    sj_fund_1 = db.Column(db.TEXT)
    sj_fund_2 = db.Column(db.TEXT)
    sj_fund_3 = db.Column(db.TEXT)
    sj_fund_4 = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_37(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    com_name = db.Column(db.TEXT)
    co_uni = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    pro_fund = db.Column(db.TEXT)
    df_mat = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_38(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    comre_name = db.Column(db.TEXT)
    re_level = db.Column(db.TEXT)
    com_name = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    com_code = db.Column(db.TEXT)
    ind = db.Column(db.TEXT)
    re_inve = db.Column(db.TEXT)
    rd_rate = db.Column(db.TEXT)
    re_per = db.Column(db.TEXT)
    high_per = db.Column(db.TEXT)
    place = db.Column(db.TEXT)
    cen_tec = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)
    kh_level = db.Column(db.TEXT)
    cate = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_39(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_name = db.Column(db.TEXT)
    sbcom_name = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    sz_reward = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_4(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    town = db.Column(db.TEXT)
    com_num = db.Column(db.TEXT)
    d_num = db.Column(db.TEXT)
    rep_rate = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_40(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_name = db.Column(db.TEXT)
    com_name = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    com_per = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    re_side = db.Column(db.TEXT)
    tec_trade = db.Column(db.TEXT)
    pl_bz = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_41(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    sat_data = db.Column(db.TEXT)
    tec_kf = db.Column(db.TEXT)
    tec_zr = db.Column(db.TEXT)
    tec_zx = db.Column(db.TEXT)
    tec_ser = db.Column(db.TEXT)
    total = db.Column(db.TEXT)
    inc = db.Column(db.TEXT)
    zzs_de = db.Column(db.TEXT)
    sds_de = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_42(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    base_name = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    egg = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_43(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    com_name = db.Column(db.TEXT)
    sb_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    egg = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_44(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    com_name = db.Column(db.TEXT)
    sb_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    egg = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_45(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    base_name = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    egg = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_46(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    com_name = db.Column(db.TEXT)
    sb_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    pos = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_47(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    com_name = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_48(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    com_name = db.Column(db.TEXT)
    sale_income = db.Column(db.TEXT)
    pro = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_49(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    base_name = db.Column(db.TEXT)
    field = db.Column(db.TEXT)
    yt_com = db.Column(db.TEXT)
    re_year = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_5(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    town = db.Column(db.TEXT)
    y_num = db.Column(db.TEXT)
    d_num = db.Column(db.TEXT)
    d_rate = db.Column(db.TEXT)
    ktd_num = db.Column(db.TEXT)
    ktd_rate = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_50(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    com_name = db.Column(db.TEXT)
    com_sit = db.Column(db.TEXT)
    town = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_51(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    com_name = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    year = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_52(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_name = db.Column(db.TEXT)
    com_name = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    pro_fund = db.Column(db.TEXT)
    sz_fund = db.Column(db.TEXT)
    ks_fund = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_53(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    year = db.Column(db.TEXT)
    level = db.Column(db.TEXT)
    agent = db.Column(db.TEXT)
    com_name = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    cer_code = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_54(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    year_2011 = db.Column(db.TEXT)
    year_2012 = db.Column(db.TEXT)
    year_2013 = db.Column(db.TEXT)
    year_2014 = db.Column(db.TEXT)
    year_2015 = db.Column(db.TEXT)
    year_2016 = db.Column(db.TEXT)
    year_2020 = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_55(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    com_group = db.Column(db.TEXT)
    com_name = db.Column(db.TEXT)
    com_loc = db.Column(db.TEXT)
    com_zt = db.Column(db.TEXT)
    field = db.Column(db.TEXT)
    com_type = db.Column(db.TEXT)
    com_capt = db.Column(db.TEXT)
    com_time = db.Column(db.TEXT)
    if_new = db.Column(db.TEXT)
    re_new_year = db.Column(db.TEXT)
    kj_fund = db.Column(db.TEXT)
    sale_sb = db.Column(db.TEXT)
    sn_sale = db.Column(db.TEXT)
    qn_sale = db.Column(db.TEXT)
    jnl_sale = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    sit_name = db.Column(db.TEXT)
    sit_level = db.Column(db.TEXT)
    res_dire = db.Column(db.TEXT)
    res_per = db.Column(db.TEXT)
    if_yf = db.Column(db.TEXT)
    if_cx = db.Column(db.TEXT)
    kj_amount = db.Column(db.TEXT)
    gj_amount = db.Column(db.TEXT)
    sb_amount = db.Column(db.TEXT)
    ds_amount = db.Column(db.TEXT)
    xq_amount = db.Column(db.TEXT)
    qy_amount = db.Column(db.TEXT)
    yftd_per = db.Column(db.TEXT)
    bs_per = db.Column(db.TEXT)
    ss_per = db.Column(db.TEXT)
    bk_per = db.Column(db.TEXT)
    dz_per = db.Column(db.TEXT)
    gj_per = db.Column(db.TEXT)
    zj_per = db.Column(db.TEXT)
    lj_per = db.Column(db.TEXT)
    zj_amount = db.Column(db.TEXT)
    fmzl_amount = db.Column(db.TEXT)
    sxzl_amount = db.Column(db.TEXT)
    yf_name = db.Column(db.TEXT)
    yfsb_xh = db.Column(db.TEXT)
    amount = db.Column(db.TEXT)
    gzfs = db.Column(db.TEXT)
    gzsj = db.Column(db.TEXT)
    price = db.Column(db.TEXT)
    dq_problem = db.Column(db.TEXT)
    range = db.Column(db.TEXT)
    sol_tec_index = db.Column(db.TEXT)
    gn_sit = db.Column(db.TEXT)
    rc_xq = db.Column(db.TEXT)
    xq_je = db.Column(db.TEXT)
    sy_period = db.Column(db.TEXT)
    product = db.Column(db.TEXT)
    profile = db.Column(db.TEXT)
    tec_index = db.Column(db.TEXT)
    app_sit = db.Column(db.TEXT)
    other = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_6(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    code = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    com_name = db.Column(db.TEXT)
    field = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    rec_tiem = db.Column(db.TEXT)
    aplogua_amout = db.Column(db.TEXT)
    hagua_amount = db.Column(db.TEXT)
    cgua_amount = db.Column(db.TEXT)
    cop_amount = db.Column(db.TEXT)
    act_amount = db.Column(db.TEXT)
    co_bank = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_7(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    com_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    if_tw = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    time = db.Column(db.TEXT)
    loan_rc = db.Column(db.TEXT)
    loan_sx = db.Column(db.TEXT)
    zd_num = db.Column(db.TEXT)
    fd_time = db.Column(db.TEXT)
    loan_term = db.Column(db.TEXT)
    loan_rate = db.Column(db.TEXT)
    lj_loan = db.Column(db.TEXT)
    hk_num = db.Column(db.TEXT)
    tx_num = db.Column(db.TEXT)
    dc_num = db.Column(db.TEXT)
    loan_ye = db.Column(db.TEXT)
    y_bxj = db.Column(db.TEXT)
    co_bank = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    xc_sx = db.Column(db.TEXT)
    sig_sit = db.Column(db.TEXT)
    online_sb = db.Column(db.TEXT)
    sm_cl = db.Column(db.TEXT)
    sz_code = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_8(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    num = db.Column(db.TEXT)
    p_name = db.Column(db.TEXT)
    com_name = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    if_tw = db.Column(db.TEXT)
    year = db.Column(db.TEXT)
    time = db.Column(db.TEXT)
    loan_rc = db.Column(db.TEXT)
    loan_sx = db.Column(db.TEXT)
    zd_num = db.Column(db.TEXT)
    fd_time = db.Column(db.TEXT)
    loan_term = db.Column(db.TEXT)
    loan_rate = db.Column(db.TEXT)
    lj_loan = db.Column(db.TEXT)
    hk_num = db.Column(db.TEXT)
    tx_num = db.Column(db.TEXT)
    dc_num = db.Column(db.TEXT)
    loan_ye = db.Column(db.TEXT)
    y_bxj = db.Column(db.TEXT)
    co_bank = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    xc_sx = db.Column(db.TEXT)
    sig_sit = db.Column(db.TEXT)
    online_sb = db.Column(db.TEXT)
    sm_cl = db.Column(db.TEXT)
    sz_code = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)


class result_9(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    p_name1 = db.Column(db.TEXT)
    c_com = db.Column(db.TEXT)
    p_name2 = db.Column(db.TEXT)
    town = db.Column(db.TEXT)
    lx_year = db.Column(db.TEXT)
    fund = db.Column(db.TEXT)
    com_sub = db.Column(db.TEXT)
    sub_rate = db.Column(db.TEXT)
    fi_bk = db.Column(db.TEXT)
    ficom_sub = db.Column(db.TEXT)
    fi_mat = db.Column(db.TEXT)
    se_bk = db.Column(db.TEXT)
    se_sub = db.Column(db.TEXT)
    se_mat = db.Column(db.TEXT)
    th_bk = db.Column(db.TEXT)
    th_sub = db.Column(db.TEXT)
    th_mat = db.Column(db.TEXT)
    fo_bk = db.Column(db.TEXT)
    fo_sub = db.Column(db.TEXT)
    fo_mat = db.Column(db.TEXT)
    fi_bk = db.Column(db.TEXT)
    fi_sub = db.Column(db.TEXT)
    fi_mat = db.Column(db.TEXT)
    si_bk = db.Column(db.TEXT)
    si_sub = db.Column(db.TEXT)
    si_mat = db.Column(db.TEXT)
    ks_mat = db.Column(db.TEXT)
    contact = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    remark = db.Column(db.TEXT)

    def __repr__(self):
        return 'info:{}'.format(self.id)

    def __init__(self, columns, data):
        init_databse(self, columns, data)
