SELECT
 u.id
,u.gender
,u.age
,u.region_code
,u.policy_sales_channel
,v.driving_license
,v.vehicle_age
,v.vehicle_damage
,i.previously_insured
,i.annual_premium
,i.vintage
,i.response
FROM 
pa004.users u 
    LEFT JOIN pa004.vehicle v ON u.id = v.id 
    LEFT JOIN pa004.insurance i ON u.id = i.id