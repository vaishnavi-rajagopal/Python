# python SB_deploy.py <object_type> <deploy/backup/enable/disable/delete> <target_env> <source_env> 
# Example : python SB_deploy.py trigger backup PROD DEV
# Object Type can be task, triggers, scripts, variables;
# <source_env> is optional and is used only for deploy activity
# enable and disable activity is only used for Trigger objects.

import sys
import requests
import keyring
import xml.etree.ElementTree as ET
header = { 'Content-Type' : 'application/xml' }

#Credential Retreival
passwd = keyring.get_password("PAM", "vaverma")

obj_type=str(sys.argv[1])
v_action = str(sys.argv[2])
target_env = str(sys.argv[3])
if len(sys.argv) < 5:
	source_env =''
else:
	source_env = str(sys.argv[4])

def deploy(url,param, header):

	res_del = requests.put(url, auth=('vaverma', passwd), data = param, headers=header)
	if res_del.status_code==404:
		res_del = requests.post(url, auth=('vaverma', passwd), data = param, headers=header)
	print res_del.text
	return;

def delete(url,header):

	res_del = requests.delete(url, auth=('vaverma', passwd), headers=header)
	print res_del.text
	return;

def backup(url,o_name):

	res_bkp = requests.get(url, auth=('vaverma', passwd))
	file_name=o_name+'.xml'
	with open(file_name, 'wb') as file:
		file.write(res_bkp.content)
	return;

def enable_disable_trg(t_env,param):	

	url='https://'+t_env+'/opswise/resources/trigger/ops-enable-disable-trigger'
	res_en = requests.post(url, auth=('vaverma', passwd), data = param, headers=header)
	print res_en.text
	return;

def main():
	#List of Objects to be updated
	with open('list.txt', 'r') as file:
	    task=file.readlines()
	depth_main=len(task)

	if source_env.upper() == 'DEV': 
		s_env_var='emsbucdev'
	elif source_env.upper() == 'TEST': 
		s_env_var='emsbuctst'
	elif source_env.upper() == 'MAUI': 
		s_env_var='emsbuce2e'
	elif source_env.upper() == 'PREPROD': 
		s_env_var='emsbuccppe'
	elif source_env.upper() == 'PROD': 
		s_env_var='emsbuccprd'

	if target_env.upper() == 'DEV': 
		t_env_var='emsbucdev'
	elif target_env.upper() == 'TEST': 
		t_env_var='emsbuctst'
	elif target_env.upper() == 'MAUI': 
		t_env_var='emsbuce2e'
	elif target_env.upper() == 'PREPROD': 
		t_env_var='emsbuccppe'
	elif target_env.upper() == 'PROD': 
		t_env_var='emsbuccprd'

	#loop for every task
	for t in range(0,depth_main):

		obj_name=task[t].rstrip("\n")
		tgt_url = 'https://'+t_env_var+'/opswise/resources/'+obj_type+'?'+obj_type+'name='+obj_name

		if v_action.lower()== 'backup':
			backup(tgt_url,obj_name)

		if v_action.lower()== 'deploy':
			src_url = 'https://'+s_env_var+'/opswise/resources/'+obj_type+'?'+obj_type+'name='+obj_name
			response = requests.get(src_url, auth=('vaverma', passwd))
			if response.status_code==404:
				print ('obj_name not found '+ obj_name)
			else:
				file_name=obj_name+'.xml'
				with open(file_name, 'wb') as file:
					file.write(response.content)

				tree = ET.parse(file_name)
				root = tree.getroot()
				param=ET.tostring(root, encoding='utf-8', method='xml')
				deploy(tgt_url,param,header)

		if v_action.lower() in ('enable','disable'):
			if v_action=='enable': v_act='true'
			else: v_act='false'
			with open('data.xml', 'wb') as file:
				file.write('<enable-disable-trigger><trigger enable="'+v_act+'" name="'+obj_name+'"></trigger></enable-disable-trigger>')

			tree = ET.parse('data.xml')
			root = tree.getroot()
			param=ET.tostring(root, encoding='utf-8', method='xml')
			enable_disable_trg(t_env_var,param)

		if v_action.lower()== 'delete':
				delete(tgt_url,header)

	return;

main()
