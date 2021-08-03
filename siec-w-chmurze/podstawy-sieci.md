
```
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Simple Network'
Resources:

    VPC:
        Type: AWS::EC2::VPC
        Properties:
            CidrBlock: "10.0.0.0/16"
            EnableDnsHostnames: True
            EnableDnsSupport: True
            Tags:
                - Key: Name
                  Value: !Sub ${AWS::StackName}-VPC
    SubnetPublic1:
      Type: "AWS::EC2::Subnet"
      Properties:
        AvailabilityZone : "eu-west-1a"
        CidrBlock: "10.0.1.0/24"
        MapPublicIpOnLaunch: True
        VpcId:
          Ref: VPC
        Tags:
          - Key: Name
            Value: !Sub ${AWS::StackName}-PUB_1

    SubnetPublic2:
      Type: "AWS::EC2::Subnet"
      Properties:
        AvailabilityZone : "eu-west-1b"
        CidrBlock: "10.0.3.0/24"
        MapPublicIpOnLaunch: True
        VpcId:
          Ref: VPC
        Tags:
          - Key: Name
            Value: !Sub ${AWS::StackName}-PUB_2

    SubnetPrivate1:
      Type: "AWS::EC2::Subnet"
      Properties:
        AvailabilityZone : "eu-west-1a"
        CidrBlock: "10.0.2.0/24"
        MapPublicIpOnLaunch: True
        VpcId:
          Ref: VPC
        Tags:
          - Key: Name
            Value: !Sub ${AWS::StackName}-PRV_1

    SubnetPrivate2:
      Type: "AWS::EC2::Subnet"
      Properties:
        AvailabilityZone : "eu-west-1b"
        CidrBlock: "10.0.4.0/24"
        MapPublicIpOnLaunch: True
        VpcId:
          Ref: VPC
        Tags:
          - Key: Name
            Value: !Sub ${AWS::StackName}-PRV_2

    InternetGateway:
        Type: AWS::EC2::InternetGateway
        Properties:
            Tags:
                - Key: Name
                  Value: !Sub ${AWS::StackName}-IGW

    InternetGatewayAttachment:
        Type: AWS::EC2::VPCGatewayAttachment
        Properties:
            InternetGatewayId: !Ref InternetGateway
            VpcId: !Ref VPC

    PublicRouteTable:
        Type: AWS::EC2::RouteTable
        Properties:
            VpcId: !Ref VPC
            Tags:
                - Key: Name
                  Value: !Sub ${AWS::StackName}-PublicRouteTable

    DefaultPublicRoute:
        Type: AWS::EC2::Route
        DependsOn: InternetGatewayAttachment
        Properties:
            RouteTableId: !Ref PublicRouteTable
            DestinationCidrBlock: 0.0.0.0/0
            GatewayId: !Ref InternetGateway

    PublicSubnet1RouteTableAssociation:
        Type: AWS::EC2::SubnetRouteTableAssociation
        Properties:
            RouteTableId: !Ref PublicRouteTable
            SubnetId: !Ref SubnetPublic1

    PublicSubnet2RouteTableAssociation:
        Type: AWS::EC2::SubnetRouteTableAssociation
        Properties:
            RouteTableId: !Ref PublicRouteTable
            SubnetId: !Ref SubnetPublic2


Outputs:
    VpcId: 
        Value: !Ref VPC
    PublicSubnet1:
        Value: !Ref SubnetPublic1     
    PublicSubnet2:
        Value: !Ref SubnetPublic2
    PrivateSubnet1:
        Value: !Ref SubnetPrivate1
    PrivateSubnet2:
        Value: !Ref SubnetPrivate2
```