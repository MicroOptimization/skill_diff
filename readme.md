# Skill Diff (Working name)
This project is gonna help people who are breaking into a new industry
or new grads who have to learn practical fields to get situated in the
job market. 

This is gonna be a data analytics tool that'll identify demand in any 
particular job market and also tell you the most common skills 
and later what skills have the smallest ratio of applicants to skill freq.

## There's gonna be two main parts to this
1. A web scraper
   - For now this'll scrape linkedin. 
   - The input is going to be search terms. For example: 
"flask python developer" or "marketing intern"
   - This will scrape *every single job listing* for the search
   - We're gonna implement exclusions and inclusions for keywords later, and
probably location filtering
  
2. A keyword analyzer
   - This is gonna check for the frequency of job specific keywords
   - For example "NodeJS", "MySQL", "c++", "AWS" will pass our filter
   - We're later going to compare it to the number of applicants for a 
particular job