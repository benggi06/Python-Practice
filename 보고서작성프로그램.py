for date in range(1,51):
    with open('{0}주차.txt'.format(date),'w',encoding='utf8') as report_file:
        report_file.write('- {0} 주차 주간보고 -'.format(date))
        report_file.write('\n부서 : ')
        report_file.write('\n이름 : ')
        report_file.write('\n업무 요약 : ')