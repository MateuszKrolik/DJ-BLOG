import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import {
  DockerImageFunction,
  DockerImageCode,
  FunctionUrlAuthType,
  Architecture,
} from 'aws-cdk-lib/aws-lambda';
import * as ssm from 'aws-cdk-lib/aws-ssm';

export class AwsCdkInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Retrieve secrets from SSM Parameter Store
    const secretKey = ssm.StringParameter.valueForStringParameter(
      this,
      '/django-blog/SECRET_KEY'
    );
    const appHost = ssm.StringParameter.valueForStringParameter(
      this,
      '/django-blog/APP_HOST'
    );
    const dbUser = ssm.StringParameter.valueForStringParameter(
      this,
      '/django-blog/DB_USER'
    );
    const dbPassword = ssm.StringParameter.valueForStringParameter(
      this,
      '/django-blog/DB_PASSWORD'
    );
    const dbHost = ssm.StringParameter.valueForStringParameter(
      this,
      '/django-blog/DB_HOST'
    );
    const awsStorageBucketName = ssm.StringParameter.valueForStringParameter(
      this,
      '/django-blog/AWS_STORAGE_BUCKET_NAME'
    );
    const awsS3RegionName = ssm.StringParameter.valueForStringParameter(
      this,
      '/django-blog/AWS_S3_REGION_NAME'
    );
    const dbName = ssm.StringParameter.valueForStringParameter(
      this,
      '/django-blog/DB_NAME'
    );

    // The code that defines your stack goes here
    const apiImageCode = DockerImageCode.fromImageAsset('../app', {
      cmd: ['lambda_handler.handler'],
      buildArgs: {
        platform: 'linux/amd64',
      },
    });
    // Public URL for the API function.
    const apiFunction = new DockerImageFunction(this, 'ApiFunc', {
      code: apiImageCode,
      memorySize: 128,
      timeout: cdk.Duration.seconds(10),
      architecture: Architecture.X86_64,
      environment: {
        SECRET_KEY: secretKey,
        IS_DEVELOPMENT: 'False',
        APP_HOST: appHost,
        DB_USER: dbUser,
        DB_PASSWORD: dbPassword,
        DB_HOST: dbHost,
        DB_NAME: dbName,
        DB_PORT: '50013', 
        AWS_STORAGE_BUCKET_NAME: awsStorageBucketName,
        AWS_S3_REGION_NAME: awsS3RegionName,
      },
    });

    // Public URL for the API function.
    const functionUrl = apiFunction.addFunctionUrl({
      authType: FunctionUrlAuthType.NONE,
    });

    // Output the URL for the API function.
    new cdk.CfnOutput(this, 'FunctionUrl', {
      value: functionUrl.url,
    });
  }
}
