#Su dung bang ma ASCII
cipher = ('Uz odkbfasdmbtk, m Omqemd oubtqd, mxea wzaiz me Omqemd\'e oubtqd, ftq eturf oubtqd, Omqemd\'e oapq ad Omqemd eturf, ue azq ar ftq euybxqef mzp yaef iupqxk wzaiz qzodkbfuaz fqotzucgqe. Uf ue m fkbq ar egnefufgfuaz oubtqd uz ituot qmot xqffqd uz ftq bxmuzfqjf ue dqbxmoqp nk m xqffqd eayq rujqp zgynqd ar baeufuaze paiz ftq mxbtmnqf. Rad qjmybxq, iuft m xqrf eturf ar 3, P iagxp nq dqbxmoqp nk M, Q iagxp nqoayq N, mzp ea az. Ftq yqftap ue zmyqp mrfqd Vgxuge Omqemd, ita geqp uf uz tue bduhmfq oaddqebazpqzoq.u tabq kag pupzf fdmzexmfq uf nk tmzp. ftmfe itmf oaybgfqde mdq rad. pauzs uf uz nk tmzp ue uzqrruouqzf mzp ftmf\'e itk ftue fqjf ue ea xazs. geuzs efduzs.ymwqfdmze() ue dqoayyqzpqp')
S = ""
key = 1
while key <= 26:
	for i in cipher:
		if i.isalpha() == False:
			S = S + i
		else:
			var = ord(i) #chuyen mot ky tu thanh mot gia tri nguyen trong bang ma ASCII
			var += key
			if i == i.upper():
				if var > ord('Z') :
					var -= 26
				S = S + chr(var) #chuyen mot gia tri nguyen thanh mot ky tu trong bang ma ASCII va thuc hien noi chuoi 
			else:
				if var > ord('z') :
					var -= 26
				S = S + chr(var)
	print "Key",key, S,"\n"
	S = ""
	key += 1
