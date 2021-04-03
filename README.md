Questions/comments/suggestions? Reach me via Twitter @cxteam_lim <br>

Official DOH announcements/updates are at https://ncovtracker.doh.gov.ph<br>

### Important: The dataset used here is part of the 'DOH Data Drop'. A full description and the download link is contained in the README file at https://bit.ly/DataDropPH

#### Snippet from the Data Drop README file regarding the dataset that is used by this repo
> Health Facility Capacity from the DOH Data Collect <br>
> Health facility data as of 8:00 AM is encoded and submitted daily, for bed occupancy and
> mechanical ventilator utilization as intended for Covid-19 cases, and weekly, for select
> logistics inventory, by hospitals and infirmaries through the DOH DataCollect BedTracker
> App v4.1.
> Submitted data as of 11:59PM of the previous day is extracted for analysis. The last
> observation carried forward (LOCF) imputation method is being implemented to correct for
> missing values incurred by non-submission of some health facilities for the current cut-off
> date of analysis. The most recent submission in the last 14 days of each unique facility is
> extracted and analyzed. This step is necessary so that the total number of beds and equipment
> will not be affected by the daily submission rate. As of August 5, 2020, the overall response
> rates for the DOH DataCollect BedTracker App are at 98.3% for hospitals and 97.5% for
> infirmaries. Summary estimates are released on DOH Facebook and BeatCovid Situationer
> every 4pm of the current day.

### Very important: Please contact the ONE HOSPITAL COMMAND CENTER if you are looking for a hospital room / healthcare referral.
The agents at the ONE HOSPITAL COMMAND CENTER have access to more recent data. Reach them through the ff. numbers:
(02) 8865-0500, 0915-777-7777 and 0919-977-3333. Source:
https://doh.gov.ph/press-release/ONE-HOSPITAL-COMMAND-CENTER-REPORTS-90-percent-SUCCESS-RATE <br><br>
DOH COVID-19 toll-free hotline number: 1555 

As mentioned in the 30 March 2021 House hearing https://www.youtube.com/watch?v=BOZ25Ed0A78 (start at around the 2hr mark), 
there are other factors that influence a hospital's capacity to accept more patients: availability of healthcare workers, 
supplies (medicines, O2, ...), etc. 

[Hospital vacancies extracted from the 'DOH Data Drop'](https://github.com/maytlim/doh_data/blob/main/vacancies.ipynb) in NCR for the 3 days prior to DOH data reporting. Legend: _v = vacant, _o = occupied, icu = intensive care unit, isolbed = isolation, beds_ward = beds in a converted ward (for confirmed cases only), mechvent = mechanical ventilator. These values are specific for COVID-19 cases. 

[Hospital (non-covid) vacancies extracted from the 'DOH Data Drop'](https://github.com/maytlim/doh_data/blob/main/vacancies-noncovid.ipynb) - The beds allocated the non-COVID patients are tagged with _nc), e.g. icu_v_nc means vacant ICU bed for non-COVID patients.
