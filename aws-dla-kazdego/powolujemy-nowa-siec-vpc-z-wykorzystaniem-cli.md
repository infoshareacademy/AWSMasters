
```
#Creating VPC Network
export VPC=$(aws ec2 create-vpc --cidr-block "10.0.0.0/16" --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=awsmasters-network}]' --output text --query Vpc.VpcId)

#Creating Subnets
export SUBNET_PUB_1=$(aws ec2 create-subnet --vpc-id $VPC --cidr-block "10.0.1.0/24" --availability-zone eu-west-1a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=awsmasters_pub_1}]' --output text --query Subnet.SubnetId)
export SUBNET_PUB_2=$(aws ec2 create-subnet --vpc-id $VPC --cidr-block "10.0.2.0/24" --availability-zone eu-west-1b --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=awsmasters_pub_2}]' --output text --query Subnet.SubnetId)
export SUBNET_PRV_1=$(aws ec2 create-subnet --vpc-id $VPC --cidr-block "10.0.3.0/24" --availability-zone eu-west-1a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=awsmasters_prv_1}]' --output text --query Subnet.SubnetId)
export SUBNET_PRV_2=$(aws ec2 create-subnet --vpc-id $VPC --cidr-block "10.0.4.0/24" --availability-zone eu-west-1b --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=awsmasters_prv_2}]' --output text --query Subnet.SubnetId)

#Create Internet Gateway
export IGW=$(aws ec2 create-internet-gateway --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=awsmasters_igw}]' --output text --query InternetGateway.InternetGatewayId)
aws ec2 attach-internet-gateway --internet-gateway-id $IGW --vpc-id $VPC

#Create Routing
export ROUTE_TABLE=$(aws ec2 create-route-table --vpc-id $VPC --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=awsmasters_rt}]' --output text --query RouteTable.RouteTableId)
aws ec2 create-route --destination-cidr-block "0.0.0.0/0" --route-table-id $ROUTE_TABLE --gateway-id $IGW
aws ec2 associate-route-table --route-table-id $ROUTE_TABLE --subnet-id $SUBNET_PUB_1
aws ec2 associate-route-table --route-table-id $ROUTE_TABLE --subnet-id $SUBNET_PUB_2

#Auto-Assign Public IP for Public Subnets
aws ec2 modify-subnet-attribute --subnet-id $SUBNET_PUB_1 --map-public-ip-on-launch
aws ec2 modify-subnet-attribute --subnet-id $SUBNET_PUB_2 --map-public-ip-on-launch

```
