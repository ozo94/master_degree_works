# coding=utf-8

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

        setattr(self, columns[index], value)


class sums_1(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	gdp= db.Column(db.TEXT)
	fund= db.Column(db.TEXT)
	fund_rate= db.Column(db.TEXT)
	local_fund= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_10(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	res_ws= db.Column(db.TEXT)
	ac_ws_gov= db.Column(db.TEXT)
	ac_ws_sz= db.Column(db.TEXT)
	gov_res_center= db.Column(db.TEXT)
	gov_imp_ins= db.Column(db.TEXT)
	out_gov_res_ins= db.Column(db.TEXT)
	zs_eng_res_center= db.Column(db.TEXT)
	sz_res_all= db.Column(db.TEXT)
	sz_res_outsea= db.Column(db.TEXT)
	com_res_gov= db.Column(db.TEXT)
	com_res_sz= db.Column(db.TEXT)
	imp_res_gov= db.Column(db.TEXT)
	imp_res_sz= db.Column(db.TEXT)
	ins_taiwan= db.Column(db.TEXT)
	ks_res_ins= db.Column(db.TEXT)
	ins_outsea= db.Column(db.TEXT)
	ins_inland= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_11(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	local= db.Column(db.TEXT)
	res_num_all= db.Column(db.TEXT)
	res_num_inland= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)

class sums_12(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	pro_over_gov= db.Column(db.TEXT)
	money_over_gov= db.Column(db.TEXT)
	pro_over_sz= db.Column(db.TEXT)
	pro_over_sz= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)

class sums_13(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	pro_863_973= db.Column(db.TEXT)
	inter_com_pro= db.Column(db.TEXT)
	pro_nation_fund= db.Column(db.TEXT)
	nation_tec_big= db.Column(db.TEXT)
	nation_imp_pro= db.Column(db.TEXT)
	torch_pro= db.Column(db.TEXT)
	star_pro= db.Column(db.TEXT)
	gov_result= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)

class sums_14(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	pro_863_973= db.Column(db.TEXT)
	inter_com_pro= db.Column(db.TEXT)
	pro_nation_fund= db.Column(db.TEXT)
	nation_tec_big= db.Column(db.TEXT)
	nation_imp_pro= db.Column(db.TEXT)
	torch_pro= db.Column(db.TEXT)
	star_pro= db.Column(db.TEXT)
	gov_result= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_15(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	zt_name= db.Column(db.TEXT)
	local= db.Column(db.TEXT)
	local_suitation= db.Column(db.TEXT)
	indetity_time= db.Column(db.TEXT)
	department= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_16(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	min_tax= db.Column(db.TEXT)
	com_tax= db.Column(db.TEXT)
	other_tax= db.Column(db.TEXT)
	sums= db.Column(db.TEXT)
	benefit_com= db.Column(db.TEXT)
	min_com= db.Column(db.TEXT)
	min_money= db.Column(db.TEXT)
	high_tech_com_tax= db.Column(db.TEXT)
	high_tech_com_num= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_17(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	reg_contract= db.Column(db.TEXT)
	contract_money= db.Column(db.TEXT)
	trade_money= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_18(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	pro_over_gov= db.Column(db.TEXT)
	money_over_gov= db.Column(db.TEXT)
	ipt_city= db.Column(db.TEXT)
	tech_money_rate= db.Column(db.TEXT)
	year_new_tech_num= db.Column(db.TEXT)
	eff_high_new_num= db.Column(db.TEXT)
	opt_high_tech= db.Column(db.TEXT)
	high_new_big_rate= db.Column(db.TEXT)
	wr_pat_num= db.Column(db.TEXT)
	pat_yer= db.Column(db.TEXT)
	res_ws_gov= db.Column(db.TEXT)
	ac_ws_gov= db.Column(db.TEXT)
	res_gov= db.Column(db.TEXT)
	qianren_define= db.Column(db.TEXT)
	creation_team= db.Column(db.TEXT)
	double_creation= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_2(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	ks= db.Column(db.TEXT)
	sz= db.Column(db.TEXT)
	js= db.Column(db.TEXT)
	nation= db.Column(db.TEXT)
	local_opt_val= db.Column(db.TEXT)
	industry_opt_val= db.Column(db.TEXT)
	res_ipt= db.Column(db.TEXT)
	sz_rec_rate= db.Column(db.TEXT)
	sz_rec_money= db.Column(db.TEXT)
	sz_rc_rate= db.Column(db.TEXT)
	sz_rc_money= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_3(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	torch_com= db.Column(db.TEXT)
	creation_com= db.Column(db.TEXT)
	gxjs_identity= db.Column(db.TEXT)
	gxjs_effictive= db.Column(db.TEXT)
	advance_com= db.Column(db.TEXT)
	gov_creation_com= db.Column(db.TEXT)
	folk_com= db.Column(db.TEXT)
	tech_mic_com= db.Column(db.TEXT)
	con_imp_product= db.Column(db.TEXT)
	con_creation_product= db.Column(db.TEXT)
	gov_eff_product= db.Column(db.TEXT)
	gov_creation_product= db.Column(db.TEXT)
	gov_imp_product= db.Column(db.TEXT)
	sz_eff_product= db.Column(db.TEXT)
	soft_com= db.Column(db.TEXT)
	soft_product= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_4(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	industry_money= db.Column(db.TEXT)
	big_ind_money= db.Column(db.TEXT)
	high_tec_ind= db.Column(db.TEXT)
	big_ind_rate= db.Column(db.TEXT)
	new_ind_money= db.Column(db.TEXT)
	new_big_ind_rate= db.Column(db.TEXT)
	last_year_rate= db.Column(db.TEXT)
	high_tec_inp= db.Column(db.TEXT)
	industry_inp= db.Column(db.TEXT)
	high_tec_ind_rate= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_5(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	high_tec_ind= db.Column(db.TEXT)
	big_ind_rate= db.Column(db.TEXT)
	new_ind_money= db.Column(db.TEXT)
	new_big_ind_rate= db.Column(db.TEXT)
	high_tec_inp= db.Column(db.TEXT)
	industry_inp= db.Column(db.TEXT)
	high_tec_ind_rate= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_6(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	local= db.Column(db.TEXT)
	high_tec_ind_num= db.Column(db.TEXT)
	m_opt= db.Column(db.TEXT)
	sums_opt= db.Column(db.TEXT)
	c_rate= db.Column(db.TEXT)
	rate= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_7(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	patent_apply= db.Column(db.TEXT)
	apl_pct= db.Column(db.TEXT)
	apl_creation= db.Column(db.TEXT)
	apl_use= db.Column(db.TEXT)
	apl_out= db.Column(db.TEXT)
	pat_num= db.Column(db.TEXT)
	pat_creation= db.Column(db.TEXT)
	pat_use= db.Column(db.TEXT)
	pat_out= db.Column(db.TEXT)
	pat_wr_num= db.Column(db.TEXT)
	eff_creation= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_8(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	patent_apply= db.Column(db.TEXT)
	apl_pct= db.Column(db.TEXT)
	apl_creation= db.Column(db.TEXT)
	apl_use= db.Column(db.TEXT)
	apl_out= db.Column(db.TEXT)
	pat_num= db.Column(db.TEXT)
	pat_creation= db.Column(db.TEXT)
	pat_use= db.Column(db.TEXT)
	pat_out= db.Column(db.TEXT)
	pat_wr_num= db.Column(db.TEXT)
	eff_creation= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)


class sums_9(db.Model):
	id= db.Column(db.INTEGER, primary_key=True)
	year= db.Column(db.TEXT)
	ac_workstation_gov= db.Column(db.TEXT)
	ac_workstation_sz= db.Column(db.TEXT)
	master_ws= db.Column(db.TEXT)
	qianren_all= db.Column(db.TEXT)
	qianren_coustom= db.Column(db.TEXT)
	wanren= db.Column(db.TEXT)
	tec_plan= db.Column(db.TEXT)
	gov_in_team_tec= db.Column(db.TEXT)
	gov_in_team_all= db.Column(db.TEXT)
	gov_in_team_other= db.Column(db.TEXT)
	gov_in_person_tec= db.Column(db.TEXT)
	gov_in_person= db.Column(db.TEXT)
	gs_person_tec= db.Column(db.TEXT)
	gs_person_other= db.Column(db.TEXT)
	gs_team= db.Column(db.TEXT)
	ks_team= db.Column(db.TEXT)
	ks_person= db.Column(db.TEXT)
	union_project= db.Column(db.TEXT)
	union_base= db.Column(db.TEXT)
	rate_con_person= db.Column(db.TEXT)
	sum_person= db.Column(db.TEXT)
	person_research= db.Column(db.TEXT)
	rate_con_tec= db.Column(db.TEXT)
	rate_sta_civ= db.Column(db.TEXT)

	def __repr__(self):
		return 'info:{}'.format(self.id)

	def __init__(self, columns, data):
		init_databse(self, columns, data)
