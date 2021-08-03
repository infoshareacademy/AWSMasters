
Frodo:
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
                  Value: !Sub ${AWS::StackName}-VPC
    SubnetPublic1:
      Type: "AWS::EC2::Subnet"
      Properties:
        AvailabilityZone : "eu-west-1a"
        CidrBlock: "11.0.1.0/24"
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
        CidrBlock: "11.0.3.0/24"
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
        CidrBlock: "11.0.2.0/24"
        VpcId:
          Ref: VPC
        Tags:
          - Key: Name
            Value: !Sub ${AWS::StackName}-PRV_1

    SubnetPrivate2:
      Type: "AWS::EC2::Subnet"
      Properties:
        AvailabilityZone : "eu-west-1b"
        CidrBlock: "11.0.4.0/24"
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
                  Value: "Frodo-Public-RT"

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

    FrodoServer:
        Type: AWS::EC2::Instance
        Properties: 
            ImageId: ami-01720b5f421cf0179
            InstanceType: t3.nano
            SecurityGroupIds: 
                - !Ref SecurityGroupSSH
            SubnetId: !Ref SubnetPublic1
            Tags:
                - Key: Name
                  Value: "Frodo"
```

Ring:
```
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Network Template'
Resources:

    VPC:
        Type: AWS::EC2::VPC
        Properties:
            CidrBlock: "12.0.0.0/16"
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
                  Value: "Ring-Public-RT"

    DefaultPublicRoute:
        Type: AWS::EC2::Route
        DependsOn: InternetGatewayAttachment
        Properties:
            RouteTableId: !Ref PublicRouteTable
            DestinationCidrBlock: 0.0.0.0/0
            GatewayId: !Ref InternetGateway

    PrivateRoute:
        Type: AWS::EC2::Route
        DependsOn: AttachGateway
        Properties:
          RouteTableId:
            Ref: PrivateRouteTable
          DestinationCidrBlock: 0.0.0.0/0
          NatGatewayId:
            Ref: NAT

    PrivateRouteTable:
        Type: AWS::EC2::RouteTable
        Properties:
          VpcId:
            Ref: VPC
          Tags:
          - Key: Name
            Value: "Ring-Private-RT"

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

    SecurityGroupWWW:
      Type: AWS::EC2::SecurityGroup
      Properties:
        GroupDescription: Limits security group egress traffic to HTTP
        SecurityGroupIngress:
        - CidrIp: 0.0.0.0/0
          IpProtocol: tcp
          ToPort: 80
          FromPort: 80
        - CidrIp: 0.0.0.0/0
          IpProtocol: tcp
          ToPort: 443
          FromPort: 443
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

    NAT:
        DependsOn: EIP
        Type: AWS::EC2::NatGateway
        Properties:
          AllocationId:
            Fn::GetAtt:
            - EIP
            - AllocationId
          SubnetId:
            Ref: SubnetPublic1

    RingServer:
        Type: AWS::EC2::Instance
        DependsOn: NAT
        Properties:
            ImageId: ami-01720b5f421cf0179
            InstanceType: t3.nano
            SecurityGroupIds:
                - !Ref SecurityGroupWWW
            SubnetId: !Ref SubnetPrivate1
            UserData: !Base64 |
                #!/bin/bash
                sudo yum update -y
                sudo yum install php httpd -y
                sudo systemctl start httpd
                sudo systemctl enable httpd
                sudo su
                cd /var/www/html
                aws s3 cp --no-sign-request s3://tomash-public/examples/php/ring/ring.jpg .
                aws s3 cp --no-sign-request s3://tomash-public/examples/php/ring/index.php .
            Tags:
                - Key: Name
                  Value: "Ring"
```