class Meltdown_Mitigation:
    
    def is_criticality_balanced(self, temperature, neutrons_emitted):
        # 1. Check for criticality
        # The first thing a control system has to do is check if the reactor is balanced in criticality. 
        # A reactor is said to be critical if it satisfies the following conditions:
        # The temperature is less than 800 K.
        # The number of neutrons emitted per second is greater than 500.
        # The product of temperature and neutrons emitted per second is less than 500000.
        # Implement the function is_criticality_balanced() that takes temperature measured in kelvin and neutrons_emitted as parameters, 
        # and returns True if the criticality conditions are met, False if not.

        if temperature < 800:
            return True
        if neutrons_emitted > 500:
            return True
        else:
            return False
        
    
    def reactor_efficiency(self, voltage, current, theoretical_max_power):
        # 2. Determine the Power output range
        # Once the reactor has started producing power its efficiency needs to be determined. Efficiency can be grouped into 4 bands:

        # green -> efficiency of 80% or more,
        # orange -> efficiency of less than 80% but at least 60%,
        # red -> efficiency below 60%, but still 30% or more,
        # black -> less than 30% efficient.
        # The percentage value can be calculated as (generated_power/theoretical_max_power)*100 where generated_power = voltage * current. 
        # Note that the percentage value is usually not an integer number, so make sure to consider the proper use of the < and <= comparisons.

        # Implement the function reactor_efficiency(<voltage>, <current>, <theoretical_max_power>), 
        # with three parameters: voltage, current, and theoretical_max_power. 
        # This function should return the efficiency band of the reactor : 'green', 'orange', 'red', or 'black'.
        
        generated_power = voltage * current
        efficiency = (generated_power/theoretical_max_power)*100
        
        if efficiency > 80:
            return 'green'
        if (efficiency < 80) and (efficiency > 60):
            return 'orange'
        if (efficiency < 60) and (efficiency > 30):
            return 'red'
        if efficiency < 30:
            return 'black'
        

    
    def fail_safe(self, temperature, neutrons_produced_per_second, threshold):
        # 3. Fail Safe Mechanism
        # Your final task involves creating a fail-safe mechanism to avoid overload and meltdown. 
        #   This mechanism will determine if the reactor is below, at, or above the ideal criticality threshold. 
        #   Criticality can then be increased, decreased, or stopped by inserting (or removing) control rods into the reactor.
        # Implement the function called fail_safe(), which takes 3 parameters: 
        #   temperature measured in kelvin, neutrons_produced_per_second, and threshold, and outputs a status code for the reactor.
        # If temperature * neutrons_produced_per_second < 90% of threshold, 
        #   output a status code of 'LOW' indicating that control rods must be removed to produce power.
        # If temperature * neutrons_produced_per_second are within plus or minus 10% of the threshold the reactor is in criticality and 
        #   the status code of 'NORMAL' should be output, indicating that the reactor is in optimum condition and control rods are in an ideal position.
        # If temperature * neutrons_produced_per_second is not in the above-stated ranges, 
        #   the reactor is going into meltdown and a status code of 'DANGER' must be passed to immediately shut down the reactor.
        
        NintyOfThreshold = (90*threshold)/100
        PlusTenOfThreshold = ((10*threshold)/100) + threshold
        MinusTenOfThreshold = threshold - ((10*threshold)/100)
        
        if (temperature * neutrons_produced_per_second) < NintyOfThreshold:
            return 'Low'

        if ((temperature * neutrons_produced_per_second) > MinusTenOfThreshold) and ((temperature * neutrons_produced_per_second) < PlusTenOfThreshold):
            return 'Normal'
        
        else:
            return 'Bad'
        
if __name__=='__main__':
    
    m = Meltdown_Mitigation()
    
    print(m.is_criticality_balanced(750,600))
    print(m.reactor_efficiency(200,50,15000))
    print(m.fail_safe(1000,30,5000))