# Validation | 验证

## Instructions

This example demonstrates how to implement validation in NestJS using class-validator and class-transformer.

### Key Concepts

- Using class-validator decorators
- ValidationPipe configuration
- DTO validation
- Custom validators
- Validation groups

### Example: DTO with Validation

```typescript
import { IsString, IsInt, Min, Max, IsEmail, IsOptional } from 'class-validator';

export class CreateCatDto {
  @IsString()
  name: string;

  @IsInt()
  @Min(0)
  @Max(20)
  age: number;

  @IsString()
  breed: string;

  @IsEmail()
  @IsOptional()
  email?: string;
}
```

### Example: ValidationPipe Configuration

```typescript
// main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ValidationPipe } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
      transform: true,
      transformOptions: {
        enableImplicitConversion: true,
      },
    }),
  );
  await app.listen(3000);
}
bootstrap();
```

### Example: Using Validation in Controller

```typescript
import { Controller, Post, Body } from '@nestjs/common';
import { CreateCatDto } from './dto/create-cat.dto';

@Controller('cats')
export class CatsController {
  @Post()
  create(@Body() createCatDto: CreateCatDto) {
    return this.catsService.create(createCatDto);
  }
}
```

### Example: Custom Validator

```typescript
import { registerDecorator, ValidationOptions, ValidationArguments } from 'class-validator';

export function IsLongerThan(property: string, validationOptions?: ValidationOptions) {
  return function (object: Object, propertyName: string) {
    registerDecorator({
      name: 'isLongerThan',
      target: object.constructor,
      propertyName: propertyName,
      constraints: [property],
      options: validationOptions,
      validator: {
        validate(value: any, args: ValidationArguments) {
          const [relatedPropertyName] = args.constraints;
          const relatedValue = (args.object as any)[relatedPropertyName];
          return typeof value === 'string' && typeof relatedValue === 'string' && value.length > relatedValue.length;
        },
      },
    });
  };
}
```

### Example: Validation Groups

```typescript
import { IsString, IsInt, ValidateIf } from 'class-validator';

export class UpdateCatDto {
  @IsString()
  @ValidateIf((o) => o.name !== undefined)
  name?: string;

  @IsInt()
  @ValidateIf((o) => o.age !== undefined)
  age?: number;
}
```

### Key Points

- Use class-validator decorators for validation rules
- ValidationPipe automatically validates DTOs
- Configure ValidationPipe for strict validation
- Transform option converts types automatically
- Create custom validators for complex rules
- Use validation groups for conditional validation
- Validation errors return 400 Bad Request
