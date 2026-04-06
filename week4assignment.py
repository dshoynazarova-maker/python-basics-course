def calculate_tickets_value(ticket_type, tickets_resolved, priority_level):
    if ticket_type=='technical':
        if priority_level=='low': tickets_value=tickets_resolved*20
        elif priority_level=='medium': tickets_value=tickets_resolved*35
        else: tickets_value=tickets_resolved*55
    elif ticket_type=='billing':
        if priority_level=='low': tickets_value=tickets_resolved*15
        elif priority_level=='medium': tickets_value=tickets_resolved*25
        else:tickets_value=tickets_resolved*40
    else:
        if priority_level=='low': tickets_value=tickets_resolved*10
        elif priority_level=='medium': tickets_value=tickets_resolved*18
        else: tickets_value = tickets_resolved*28
    return tickets_value
def calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets):
  expected_tickets=1000 + (agent_quarters * 100)
  ticket_capacity=expected_tickets - baseline_tickets
  return (resolved_tickets - baseline_tickets) / ticket_capacity * 100

def determine_performance_level(efficiency_percent):
  if efficiency_percent < 50: performance_level = 'Developing'
  elif efficiency_percent < 60: performance_level= 'Competent'
  elif efficiency_percent < 70: performance_level='Proficient'
  elif efficiency_percent < 85: performance_level='Advanced'
  else: performance_level = 'Expert'
  return performance_level
  
def calculate_performance_bonus(value, tickets, level_multiplier):
    base_bonus=value * 0.05 + tickets * 2
    if level_multiplier=='Developing':
       performance_bonus=0.5*base_bonus
    elif level_multiplier=='Competent':
       performance_bonus = base_bonus
    elif level_multiplier=='Proficient':
       performance_bonus=1.2*base_bonus
    elif level_multiplier=='Advanced':
       performance_bonus=1.5*base_bonus
    else:
      performance_bonus=1.8*base_bonus
    return round(performance_bonus, 1)

def needs_additional_training(service_weeks, total_tickets, avg_efficiency):
    if (service_weeks > 5 and avg_efficiency < 50) or (total_tickets < 100 and avg_efficiency < 60) or (service_weeks > 3 and avg_efficiency < 40):
      return 'Yes'
    else: return "No"

def generate_quality_report(agent_name, ticket_type, tickets, priority_level, agent_quarters, baseline_tickets, resolved_tickets, service_weeks):
    ticket_value=calculate_tickets_value(ticket_type, tickets, priority_level)
    resolution_efficiency=calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets)
    performance_level=determine_performance_level(resolution_efficiency)
    performance_bonus=calculate_performance_bonus(ticket_value, tickets, performance_level)
    additional_training=needs_additional_training(service_weeks, tickets, resolution_efficiency)
    print('========================================')
    print(f'Quality Report for: {agent_name}')
    print('----------------------------------------')
    print(f'Ticket Type: {ticket_type}')
    print(f'Tickets Resolved: {tickets}')
    print(f'Priority Level: {priority_level}')
    print(f'Tickets Value: ${ticket_value}') 
    print('Efficiency Analysis:')
    print(f'  Experience: {agent_quarters} quarters, Baseline: {baseline_tickets}, Resolved Tickets: {resolved_tickets}')
    print(f'  Efficiency: {resolution_efficiency:.1f}%')
    print(f'  Performance Level: {performance_level} Level')
    print(f'Performance Bonus: ${performance_bonus}')
    print(f'Service Weeks: {service_weeks}')
    print(f'Additional Training Needed: {additional_training}\n')
print('CUSTOMER SERVICE QUALITY MONITOR')
generate_quality_report("Harper", "technical", 45, "high", 3, 800, 1150, 3)
generate_quality_report("Indigo", "billing", 60, 'medium', 5, 900, 1300, 5)
generate_quality_report("Jesse", "general", 30, 'low', 8, 850, 950, 7)