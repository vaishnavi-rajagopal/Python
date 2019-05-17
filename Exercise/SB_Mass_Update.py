
import requests
import keyring
import xml.etree.ElementTree as ET
header = { 'Content-Type' : 'application/xml' }
email_tag = ['status','body','cc','emailConnection','emailTemplate','subject','to']
sysOp_tag = ['status','notificationOption','operation','task']
setVar_tag = ['status','variableScope','variableName','variableValue']


#Credential Retreival
passwd = keyring.get_password("PAM", "vaverma")
d={}

#List of Objects to be updated
with open('obj_SB2.txt', 'r') as file:
    task=file.readlines()
    depth_main=len(task)

with open('values_SB_RISK.txt', 'r') as file_val:
    d=dict([line.split(';') for line in file_val])

def email_add(root,v_status,v_body,v_cc,v_emailConnection,v_emailTemplate,v_subject,v_to):
	
	for i in range(0,len(root)):
		if root[i].tag=='actions':
			emailNotification=ET.SubElement(root[i],'emailNotification')
			for j in range(0,len(root[i])):
				if root[i][j].tag=='emailNotification':
					if len(root[i][j])==0:
						status=ET.SubElement(root[i][j],'status')
						body=ET.SubElement(root[i][j],'body')
						cc=ET.SubElement(root[i][j],'cc')
						emailConnection=ET.SubElement(root[i][j],'emailConnection')
						emailTemplate=ET.SubElement(root[i][j],'emailTemplate')
						subject=ET.SubElement(root[i][j],'subject')
						to=ET.SubElement(root[i][j],'to')
						for k in range(0,len(root[i][j])):
							text_val='v_'+root[i][j][k].tag
							root[i][j][k].text=eval(text_val)
	return root;

def email_update(root,v_status,v_body,v_cc,v_emailConnection,v_emailTemplate,v_subject,v_to,v_attachStdError,v_attachStdOut,v_stderrNumLines,v_stderrStartLine,v_stdoutNumLines,v_stdoutStartLine):
	
	for i in range(0,len(root)):
		if root[i].tag=='actions':
			for j in range(0,len(root[i])):
				if root[i][j].tag=='emailNotification':
					for k in range(0,len(root[i][j])):
						if root[i][j][k].tag in email_tag :
							text_val='v_'+root[i][j][k].tag
							root[i][j][k].text=eval(text_val)
	return root;

def sysOperation_add(root,v_status,v_notificationOption,v_operation,v_task):

	v_task=v_task+'_abort'
	for i in range(0,len(root)):
		if root[i].tag=='actions':
			systemOperation=ET.SubElement(root[i],'systemOperation')
			for j in range(0,len(root[i])):
				if root[i][j].tag=='systemOperation':
					if len(root[i][j])==0:
						status=ET.SubElement(root[i][j],'status')
						notificationOption=ET.SubElement(root[i][j],'notificationOption')
						operation=ET.SubElement(root[i][j],'operation')
						task=ET.SubElement(root[i][j],'task')
						for k in range(0,len(root[i][j])):
							text_val='v_'+root[i][j][k].tag
							root[i][j][k].text=eval(text_val)
	return root;

def sysOperation_update(root,v_status,v_notificationOption,v_operation,v_task):

	v_task=v_task+'_abort'
	for i in range(0,len(root)):
		if root[i].tag=='actions':
			for j in range(0,len(root[i])):
				if root[i][j].tag=='systemOperation':
					for k in range(0,len(root[i][j])):
						if root[i][j][k].tag in sysOp_tag :
							text_val='v_'+root[i][j][k].tag
							root[i][j][k].text=eval(text_val)
	return root;

def setVariable_add(root,v_status,v_variableScope,v_variableName,v_variableValue):

	for i in range(0,len(root)):
		if root[i].tag=='actions':
			systemOperation=ET.SubElement(root[i],'setVariableAction')
			for j in range(0,len(root[i])):
				if root[i][j].tag=='setVariableAction':
					if len(root[i][j])==0:
						status=ET.SubElement(root[i][j],'status')
						notificationOption=ET.SubElement(root[i][j],'variableScope')
						operation=ET.SubElement(root[i][j],'variableName')
						task=ET.SubElement(root[i][j],'variableValue')
						for k in range(0,len(root[i][j])) :
							text_val='v_'+root[i][j][k].tag
							root[i][j][k].text=eval(text_val)
	return root;

def setVariable_update(root,v_status,v_variableScope,v_variableName,v_variableValue):

	for i in range(0,len(root)):
		if root[i].tag=='actions':
			for j in range(0,len(root[i])):
				if root[i][j].tag=='setVariableAction':
					for k in range(0,len(root[i][j])):
						if root[i][j][k].tag in setVar_tag :
							text_val='v_'+root[i][j][k].tag
							root[i][j][k].text=eval(text_val)
	return root;

def mbs_add(root,v_opswiseGroup):

	for i in range(0,len(root)):
		if root[i].tag=='opswiseGroups':
			systemOperation=ET.SubElement(root[i],'opswiseGroup')
			for j in range(0,len(root[i])):
				if root[i][j].text is None:
					root[i][j].text=v_opswiseGroup
	return root;

def mbs_update(root,v_opswiseGroup):

	for i in range(0,len(root)):
		if root[i].tag=='opswiseGroups':
			for j in range(0,len(root[i])):
				root[i][j].text=v_opswiseGroup
	return root;

def agent_update(root,v_agentVar):

	for i in range(0,len(root)):
		if root[i].tag=='agentVar':
			root[i].text=v_agentVar
	return root;

#loop for every task
for t in range(0,depth_main):

	task_name=task[t].rstrip("\n")
	url= 'https://chelemsbuc005/opswise/resources/task?taskname='+task_name

	response = requests.get(url, auth=('vaverma', passwd))
	with open('data.xml', 'wb') as file:
		file.write(response.content)

	tree = ET.parse('data.xml')
	root = tree.getroot()
	depth_root = len(root)		

	root=email_add(root,d['status_email'].rstrip("\n"),d['body'].rstrip("\n"),d['cc'].rstrip("\n"),d['emailConnection'].rstrip("\n"),d['emailTemplate'].rstrip("\n"),d['subject'].rstrip("\n"),d['to'].rstrip("\n"))
	root=sysOperation_update(root,d['status_sysOps'].rstrip("\n"),d['notificationOption'].rstrip("\n"),d['operation'].rstrip("\n"),task_name)
	root=setVariable_add(root,d['status_setVariable1'].rstrip("\n"),d['variableScope1'].rstrip("\n"),d['variableName1'].rstrip("\n"),d['variableValue1'].rstrip("\n"))
	root=mbs_update(root,'DSP')
	root=agent_update(root,d['agentVar'].rstrip("\n"))

	param=ET.tostring(root, encoding='utf-8', method='xml')
	#print param

	req = requests.put(url, auth=('vaverma', passwd), data = param, headers=header)
	print req.text