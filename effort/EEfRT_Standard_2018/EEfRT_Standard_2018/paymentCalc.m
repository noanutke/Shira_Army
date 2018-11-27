function [payment] = paymentCalc(allData)

count = 1;
reward = 0;
if length(allData(:,1)) > 6
    for x = 6:length(allData)
        %if trial was a win trial
        if allData(x,6) ~= 'l'
            %if trial was completed
            if allData(x,5) == 1 
                %if subject chose harder task
                if allData(x,1) == 1
                    payMatrix(count) = allData(x,7);
                    reward = reward + payMatrix(count);
                    count = count+1;
                    
                %if subject chose easier task
                else 
                    payMatrix(count) = 100;
                    reward = reward + payMatrix(count);
                    count = count+1;
                    
                end
            end
        end
    end
else
    reward = 0;
end



payment = reward;

                