Log Analyer:

Map reduce based log analysis using ZeroVM


Files:

1) mapper.py:
   - creates <word, count> tuples from input file

2) reducer.py
   - creates <word, aggregate_count> tuples by aggregating
     counts from all the mappers

3) query.json
   - descriptor file for deploying and running mapper and
     reducer on ZeroVM

4) output.txt
   - file containing sorted list of <word, aggregate_count> tuples
     formed by analyzing Solum IRC meeting logs available at:
     - http://eavesdrop.openstack.org/meetings/solum_team_meeting/2013/
     - http://eavesdrop.openstack.org/meetings/solum_team_meeting/2014/

     (files used are solum_team_meeting*.log.txt)


Som interesting conclusions from output.txt:

1) Solum team 'thinks' a lot (ranked 8)

2) Solum team 'thanks' a lot (ranked 16)

3) Solum team discusses 'plan' (ranked 40) more than it discusses 'code' (ranked 45)

4) API (ranked 46) and CLI (ranked 61) discussions are in top hundred topics

5) Solum team needs to discuss more about quality assurance (rank of 'QA' 2931)


Happy hacking.


   

 
