import benchmark, os

class Planner :
	
	def __init__( self, domain, problem, index, max_time = 14400, max_mem = 2048 ) :
		self.domain = domain
		self.problem = problem
		self.noext_problem = os.path.basename(self.problem).replace( '.pddl', '' )
		self.max_time = max_time
		self.max_mem = max_mem
		self.log_file = '%s-%s-%s.log'%(self.noext_problem, index, os.path.split( os.path.split( self.problem )[0])[-1])
		self.cost = 1e7

class Metric_FF(Planner) :
	def __init__( self, domain, problem, index, max_time = 14400, max_mem = 2048 ) :
		Planner.__init__( self, domain, problem, index, max_time, max_mem )

	def execute( self ) :
		cmd_string = './ff -O -E -o %s -f %s'%(self.domain, self.problem)
		self.log = benchmark.Log( self.log_file )
		self.signal, self.time = benchmark.run( cmd_string, self.max_time, self.max_mem, self.log )
		self.gather_data()

	def gather_data( self ) :
		if self.signal == 0  :
			instream = open( self.log_file )
			for line in instream :
				line = line.strip()
				if 'Total cost of plan:' in line :
					number = line.split(':')[1].strip() 
					self.cost = float( number )
			instream.close()	

class HSP (Planner):

	def __init__( self, domain, problem, index, max_time = 14400, max_mem = 2048 ) :
		Planner.__init__( self, domain, problem, index, max_time, max_mem )
		self.upper_bound = None

	def execute( self ) :
		if self.upper_bound is None :
			ub_string = ''
		else :
			ub_string = '-ub %s'%self.upper_bound
		cmd_string = './hsp_f -strict -dba-semantics -rm -cost -rAH -use-lse -bfs %s -v 0 -ipc %s %s > %s.soln'%( ub_string, self.domain, self.problem, self.noext_problem)
		self.log = benchmark.Log( self.log_file )
		self.signal, self.time = benchmark.run( cmd_string, self.max_time, self.max_mem, self.log )
		self.gather_data()

	def gather_data( self ) :
		if self.signal == 0 and os.path.exists( '%s.soln'%self.noext_problem ) :
			instream = open( '%s.soln'%self.noext_problem )
			for line in instream :
				line = line.strip()
				if 'Not Solved' in line :
					self.cost = 1e7
				toks = line.split()
				if 'MetricValue' in toks :
					self.cost = float(toks[-1])
				
			instream.close()
	
	def get_plan( self ) :
		plan = []
		if self.signal == 0 and os.path.exists( '%s.soln'%self.noext_problem ) :
			instream = open( '%s.soln'%self.noext_problem )
			for line in instream :
				line = line.strip()
				if line[0] == ';' : continue
				head, tail = line.split(':')
				operator, trash = tail.split('[' )
				operator = operator.strip()
				plan.append( operator )	 
				
			instream.close()
		return plan
		

class LAMA (Planner):

	greedy = False

	def __init__( self, domain, problem, index,  max_time = 14400, max_mem = 2048 ) :
		Planner.__init__( self, domain, problem, index, max_time, max_mem )
		self.result = os.path.basename(self.problem).replace( '.pddl','.res' )
		self.expanded = 0
		self.generated = 0
		self.iteration = 0
		self.search_time = 0
		self.optimal = False
		self.cost = 0
		self.length = 0

	def execute( self ) :
		if LAMA.greedy :
			cmd_string = './plan-greedy %s %s %s'%( self.domain, self.problem, self.result )
		else :
			cmd_string = './plan %s %s %s'%( self.domain, self.problem, self.result)
		self.log = benchmark.Log( self.log_file )
		self.signal, self.time = benchmark.run( cmd_string, self.max_time, self.max_mem, self.log )
		self.gather_data()

	def gather_data( self ) :
		instream = open( self.log_file )
		for line in instream :
			line = line.strip()
			if "Plan length" in line :
				if "cost" in line :
					tokens = line.split(",")
					tokens = [ t.strip() for t in tokens ]
					self.length = float(tokens[0].split(':')[-1].split(' ')[1].strip())
					self.cost = float(tokens[1].split(':')[-1].strip())
				else :
					self.length = float(line.split(':')[-1].split(' ')[1].strip())
					self.cost = self.length
			if "Expanded" in line :
				tokens = line.split( " " )
				self.expanded += int( tokens[1] )
			if "Domain Name:" in line :
				tokens = line.split( " " )
				self.domain = tokens[2].strip()
			if "Task Name:" in line :
				tokens = line.split( " " )
				self.instance = tokens[2].strip()
			if "Generated" in line :
				tokens = line.split( " " )
				self.generated += int( tokens[1] )
			if "Search time" in line :
				tokens = line.split( " " )
				self.search_time += float( tokens[2] )
			if "Search iteration" in line :
				self.iteration += 1
			if "Completely explored state space -- no solution!" in line :
				self.optimal = True
			
		instream.close()


#MICHAEL
class FastDownward_LAMA (Planner):

	greedy = False

	def __init__( self, domain, problem, index,  max_time = 14400, max_mem = 2048 ) :
		Planner.__init__( self, domain, problem, index, max_time, max_mem )
		self.result = os.path.basename(self.problem).replace( '.pddl','.res' )
		self.expanded = 0
		self.generated = 0
		self.iteration = 0
		self.search_time = 0
		self.optimal = False
		self.cost = 0
		self.length = 0

	def execute( self ) :
		if LAMA.greedy :
			#cmd_string = '/home/mk/Planning/fastdownwardplanner/fast-downward.py  --alias seq-sat-lama-2011 %s %s '%( self.domain, self.problem)
			#cmd_string = '/home/mk/Planning/fastdownwardplanner/fast-downward.py  --alias lama-first %s %s '%( self.domain, self.problem)
			#cmd_string = '/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/fd-0/fast-downward.py  --alias seq-sat-lama-2011 %s %s '%( self.domain, self.problem)
			cmd_string = os.path.join('..', 'downward', 'fast-downward.py') + ' %s %s --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])"'%( self.domain, self.problem)
		else :
			#cmd_string = './plan %s %s %s'%( self.domain, self.problem, self.result)
			#cmd_string = '/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/fd-0/fast-downward.py  --alias seq-sat-lama-2011 %s %s '%( self.domain, self.problem)  #Michael. I could put the normal lama here?
			#cmd_string = '/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/fd-0/fast-downward.py %s %s --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])"'%( self.domain, self.problem)
			cmd_string = os.path.join('..', 'downward', 'fast-downward.py') + ' %s %s --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])"'%( self.domain, self.problem)
		self.log = benchmark.Log( self.log_file )
		self.signal, self.time = benchmark.run( cmd_string, self.max_time, self.max_mem, self.log )
		self.gather_data()

	def gather_data( self ) :
		instream = open( self.log_file )
		for line in instream :
			line = line.strip()
			if "Plan length" in line :
				if "cost" in line :
					tokens = line.split(",")
					tokens = [ t.strip() for t in tokens ]
					self.length = float(tokens[0].split(':')[-1].split(' ')[1].strip())
					self.cost = float(tokens[1].split(':')[-1].strip())
				else :
					self.length = float(line.split(':')[-1].split(' ')[1].strip())
					self.cost = self.length
			if "Expanded" in line :
				tokens = line.split( " " )
				self.expanded += int( tokens[1] )
			if "Domain Name:" in line :
				tokens = line.split( " " )
				self.domain = tokens[2].strip()
			if "Task Name:" in line :
				tokens = line.split( " " )
				self.instance = tokens[2].strip()
			if "Generated" in line :
				tokens = line.split( " " )
				self.generated += int( tokens[1] )
			if "Search time" in line :
				tokens = line.split( " " )
				tokens[-1] = tokens[-1].replace("s", "") #Michael FD planner has output timeformat "1.346s", where the "s" causes trouble
				self.search_time += float( tokens[-1] )
			if "Search iteration" in line :
				self.iteration += 1
			if "Completely explored state space -- no solution!" in line : #Michael it seems there it should maybe set a pseudo infinity value to self.cost
				print("HERE IT FINDS NO SOLUTION!!")
				self.optimal = True
				self.cost = 100 #Michael, this is like in the gather_data definition for the HSP planner, compare above (1e7 leads to overflow errors in hypothesis.py line 144, though, so choose smaller value
			
		instream.close()
