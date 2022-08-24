import difflib
# file_01= "/Users/iqbalc/Desktop/speech_to_text/compare_results/reference.txt"
file_01= "herr holzer was sagen sie als unbeteiligter zum thema stress stress angeblich sagt man über den stress man hat ihn nicht sondern man macht ihn sich selbst danke für die philosophische betrachtung mir ist allerdings die herstellungsweise nicht bekannt deswegen kam zum thema stress wenig raus sie testen grad eine aufzeichnung die sich aufdreht genau so aufzeichnung beenden ja das mach ma mal"
#file_02= "/Users/iqbalc/Desktop/speech_to_text/compare_results/prediction1.txt"
file_02= "er holt also sagen sie als unbeteiligter zum thema stressstress an angeblich sorgt man über den stress mahat in nicht am sondern am macht in sichdan gewärt diese philosophische betrachtung mir ist allerdings die herstellungsweise nicht bekannt des vinkane wenig zum themastress ausser zi desten konteine afzweigen aber auf de ser aufsechich beenden herrswoma"
# reference_file= open(file_01).readline()
# predicted_file= open(file_02).readline()
# compare_results= difflib.HtmlDiff().make_file(reference_file, predicted_file, file_01, file_02)
compare_results= difflib.HtmlDiff().make_file(file_01, file_02)
# creating html for comparsion
comparison_report= open("/Users/iqbalc/Desktop/speech_to_text/compare_results/comparison_report.html",'w')
comparison_report.write(compare_results)
comparison_report.close()

# import difflib
# str1 = "herr holzer was sagen sie als unbeteiligter zum thema stress stress angeblich sagt man über den stress man hat ihn nicht sondern man macht ihn sich selbst danke für die philosophische betrachtung mir ist allerdings die herstellungsweise nicht bekannt deswegen kam zum thema stress wenig raus sie testen grad eine aufzeichnung die sich aufdreht genau so aufzeichnung beenden ja das mach ma mal"
# str2 = "er hoze was sagen sie als unbetäiligte zum dema stres stres a angeblich sorgt nur über den stres ma hat ihn nicht a sondern dern macht in sich dangiwirt diese philosophische betrachtung wie es olledingst die herstellungsweise nicht bekamt deswinkani wenig zum timastras aussn sedesen konnten er oftwegneihrafea so"
# str3 = "er holt also sagen sie als unbeteiligter zum thema stressstress an angeblich sorgt man über den stress mahat in nicht am sondern am macht in sichdan gewärt diese philosophische betrachtung mir ist allerdings die herstellungsweise nicht bekannt des vinkane wenig zum themastress ausser zi desten konteine afzweigen aber auf de ser aufsechich beenden herrswoma"
# str1_lines = str1.splitlines()
# str2_lines = str2.splitlines()
# str3_lines = str3.splitlines()
# d = difflib.Differ()
# diff = d.compare(str1_lines, str3_lines)
# print('\n'.join(diff))
