
import requests
import keyring
import xml.etree.ElementTree as ET
header = { 'Content-Type' : 'application/xml' }
email_tag = ['status','body','cc','emailConnection','emailTemplate','subject','to','attachStdError','attachStdOut','stderrNumLines','stderrStartLine','stdoutNumLines','stdoutStartLine']
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

def abort_add(root,v_status,v_body,v_cc,v_emailConnection,v_emailTemplate,v_subject,v_to,v_attachStdError,v_attachStdOut,v_stderrNumLines,v_stderrStartLine,v_stdoutNumLines,v_stdoutStartLine):
	
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
						attachStdError=ET.SubElement(root[i][j],'attachStdError')
						attachStdOut=ET.SubElement(root[i][j],'attachStdOut')
						stderrNumLines=ET.SubElement(root[i][j],'stderrNumLines')
						stderrStartLine=ET.SubElement(root[i][j],'stderrStartLine')
						stdoutNumLines=ET.SubElement(root[i][j],'stdoutNumLines')
						stdoutStartLine=ET.SubElement(root[i][j],'stdoutStartLine')
						for k in range(0,len(root[i][j])):
							text_val='v_'+root[i][j][k].tag
							root[i][j][k].text=eval(text_val)
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

	root=email_update(root,d['status_email'].rstrip("\n"),d['body'].rstrip("\n"),d['cc'].rstrip("\n"),d['emailConnection'].rstrip("\n"),d['emailTemplate'].rstrip("\n"),d['subject'].rstrip("\n"),d['to'].rstrip("\n"),d['attachStdError'].rstrip("\n"),d['attachStdOut'].rstrip("\n"),d['stderrNumLines'].rstrip("\n"),d['stderrStartLine'].rstrip("\n"),d['stdoutNumLines'].rstrip("\n"),d['stdoutStartLine'].rstrip("\n"))

	param=ET.tostring(root, encoding='utf-8', method='xml')
	#print param

	req = requests.put(url, auth=('vaverma', passwd), data = param, headers=header)
	print req.text