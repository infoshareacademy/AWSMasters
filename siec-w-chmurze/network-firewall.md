```
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Network Template'
Resources:

    VPC:
        Type: AWS::EC2::VPC
        Properties:
            CidrBlock: "11.0.0.0/16"
            Tags:
                - Key: Name
                  Value: "Corporate-Network"
    FirewallSubnet:
      Type: "AWS::EC2::Subnet"
      Properties:
        AvailabilityZone : "eu-west-1a"
        CidrBlock: "11.0.1.0/24"
        MapPublicIpOnLaunch: True
        VpcId:
          Ref: VPC
        Tags:
          - Key: Name
            Value: "Firewall-Subnet"

    ProtectedSubnet:
      Type: "AWS::EC2::Subnet"
      Properties:
        AvailabilityZone : "eu-west-1a"
        CidrBlock: "11.0.2.0/24"
        MapPublicIpOnLaunch: True
        VpcId:
          Ref: VPC
        Tags:
          - Key: Name
            Value: "Protected-Subnet"

    InternetGateway:
        Type: AWS::EC2::InternetGateway
        Properties:
            Tags:
                - Key: Name
                  Value: "Corporate-IGW"

    InternetGatewayAttachment:
        Type: AWS::EC2::VPCGatewayAttachment
        Properties:
            InternetGatewayId: !Ref InternetGateway
            VpcId: !Ref VPC

    FirewallRouteTable:
        Type: AWS::EC2::RouteTable
        Properties:
            VpcId: !Ref VPC
            Tags:
                - Key: Name
                  Value: "Corporate-Firewall-RT"

    ProtectedRouteTable:
        Type: AWS::EC2::RouteTable
        Properties:
            VpcId: !Ref VPC
            Tags:
                - Key: Name
                  Value: "Corporate-Protected-RT"

    ProtectedRTRoute:
        Type: AWS::EC2::Route
        DependsOn: InternetGatewayAttachment
        Properties:
            RouteTableId: !Ref ProtectedRouteTable
            DestinationCidrBlock: 0.0.0.0/0
            GatewayId: !Ref InternetGateway

    FirewallRTRoute:
        Type: AWS::EC2::Route
        DependsOn: InternetGatewayAttachment
        Properties:
            RouteTableId: !Ref FirewallRouteTable
            DestinationCidrBlock: 0.0.0.0/0
            GatewayId: !Ref InternetGateway

    FirewallRouteTableAssociation:
        Type: AWS::EC2::SubnetRouteTableAssociation
        Properties:
            RouteTableId: !Ref FirewallRouteTable
            SubnetId: !Ref FirewallSubnet

    ProtectedPublicRouteAssociation:
        Type: AWS::EC2::SubnetRouteTableAssociation
        Properties:
            RouteTableId: !Ref ProtectedRouteTable
            SubnetId: !Ref ProtectedSubnet

    SecurityGroupSSH:
      Type: AWS::EC2::SecurityGroup
      Properties:
        GroupDescription: Limits security group egress traffic to HTTP
        SecurityGroupIngress:
        - CidrIp: 0.0.0.0/0
          IpProtocol: tcp
          ToPort: 22
          FromPort: 22
        VpcId:
          Ref: VPC

    CorporateServer:
        Type: AWS::EC2::Instance
        Properties:
            ImageId: ami-01720b5f421cf0179
            InstanceType: t3.nano
            SecurityGroupIds:
                - !Ref SecurityGroupSSH
            SubnetId: !Ref ProtectedSubnet
            Tags:
                - Key: Name
                  Value: "Corporate-Server"

```