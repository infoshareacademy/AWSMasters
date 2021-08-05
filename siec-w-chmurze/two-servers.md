

```
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Two Servers'


Parameters:
  myKeyPair:
    Description: Amazon EC2 Key Pair
    Type: "AWS::EC2::KeyPair::KeyName"

Resources:

    VPC:
        Type: AWS::EC2::VPC
        Properties:
            CidrBlock: "12.0.0.0/16"
            EnableDnsHostnames: True
            EnableDnsSupport: True
            Tags:
                - Key: Name
                  Value: !Sub ${AWS::StackName}-VPC
    SubnetPublic1:
      Type: "AWS::EC2::Subnet"
      Properties:
        AvailabilityZone : "eu-west-1a"
        CidrBlock: "12.0.1.0/24"
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
        CidrBlock: "12.0.3.0/24"
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
        CidrBlock: "12.0.2.0/24"
        VpcId:
          Ref: VPC
        Tags:
          - Key: Name
            Value: !Sub ${AWS::StackName}-PRV_1

    SubnetPrivate2:
      Type: "AWS::EC2::Subnet"
      Properties:
        AvailabilityZone : "eu-west-1b"
        CidrBlock: "12.0.4.0/24"
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
                  Value: "TwoServers-Public-RT"
    DefaultPublicRoute:
        Type: AWS::EC2::Route
        DependsOn: InternetGatewayAttachment
        Properties:
            RouteTableId: !Ref PublicRouteTable
            DestinationCidrBlock: 0.0.0.0/0
            GatewayId: !Ref InternetGateway

    PrivateRouteTable:
        Type: AWS::EC2::RouteTable
        Properties:
          VpcId:
            Ref: VPC
          Tags:
          - Key: Name
            Value: "TwoServers-Private-RT"

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

    PrivateSubnet1RouteTableAssociation:
        Type: AWS::EC2::SubnetRouteTableAssociation
        Properties:
          SubnetId:
            Ref: SubnetPrivate1
          RouteTableId:
            Ref: PrivateRouteTable

    PrivateSubnet2RouteTableAssociation:
        Type: AWS::EC2::SubnetRouteTableAssociation
        Properties:
          SubnetId:
            Ref: SubnetPrivate2
          RouteTableId:
            Ref: PrivateRouteTable

    SecurityGroupSSH:
      Type: AWS::EC2::SecurityGroup
      Properties:
        GroupDescription: Limits security group egress traffic to SSH
        SecurityGroupIngress:
        - CidrIp: 0.0.0.0/0
          IpProtocol: tcp
          ToPort: 22
          FromPort: 22
        VpcId:
          Ref: VPC

    EIP:
        Type: AWS::EC2::EIP
        DependsOn: AttachGateway
        Properties:
          Domain: vpc

    AttachGateway:
        Type: AWS::EC2::VPCGatewayAttachment
        Properties:
          VpcId:
            Ref: VPC
          InternetGatewayId:
            Ref: InternetGateway

    PublicServer:
        Type: AWS::EC2::Instance
        Properties:
            ImageId: ami-01720b5f421cf0179
            InstanceType: t3.nano
            SecurityGroupIds:
                - !Ref SecurityGroupSSH
            SubnetId: !Ref SubnetPublic1
            KeyName: !Ref myKeyPair
            Tags:
                - Key: Name
                  Value: "PublicServer"

    PrivateServer:
        Type: AWS::EC2::Instance
        Properties:
            ImageId: ami-01720b5f421cf0179
            InstanceType: t3.nano
            KeyName: !Ref myKeyPair
            SecurityGroupIds:
                - !Ref SecurityGroupSSH
            SubnetId: !Ref SubnetPrivate1
            Tags:
                - Key: Name
                  Value: "PrivateServer"
```   
        
```
aws s3 cp --no-sign-request s3://REPLACEME .
```

```
scp  -i "KEY"  WHAT_TO_COPY ec2-user@YOUR_INSTANCE_IP:NEW_NAME
```
