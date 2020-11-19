# Plan Recognition from Object Detection Traces
This method uses object bounding box overlaps in video frames, PDDL domains, and an object ontology to identify plans for ongoing tasks.

Clone with Fast-Downward planner and build it.
```
git clone --recurse-submodules
cd pictoplangit/pictoplan/external/fd
./build.py
```
Input
* Kitchen task image sequence
* Ontology about tracked objects
* Planning domain
* Set of goals
* s_0
* (list of possible actions as intermediate result)

Output
* Most likely plan and goal ranking formulated in the given PDDL domain

External programs:
* Probabilistic Plan Recognition (https://sites.google.com/site/prasplanning/file-cabinet)
* Fast Downward (http://www.fast-downward.org/)
* Val (https://nms.kcl.ac.uk/planning/software/val.html)

A preliminary workshop paper of this project can be found at http://www.planrec.org/PAIR/PAIR%2020/Resource_files/PAIR20papers.zip .